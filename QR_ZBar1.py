#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import pyzbar.pyzbar as pyzbar
import csv
import time


def display(decoded_codes, image):

    # loop over the detected barcodes
    for code in decoded_codes:

        # extract the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image

        (x, y, w, h) = code.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first

        codeData = code.data.decode('utf-8')

        # draw the barcode data and barcode type on the image

        text = '{}'.format(codeData)
        cv2.putText(
            image,
            text,
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            2,
            )
    return image

def populatecsv(decoded_codes):
    for code in decoded_codes:
        codeData = code.data.decode('utf-8')
        datalist=[time.time(),codeData]
        with open('data.csv', 'a') as csvFile:
            wr = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
            wr.writerow(datalist)
        csvFile.close()


cap = cv2.VideoCapture(0)
print(cap.isOpened())
while cap.isOpened():
    (ret, frame) = cap.read()
    print(ret)
    print(frame)
    decoded_codes = pyzbar.decode(cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
    display_image = display(decoded_codes, frame)
    populatecsv(decoded_codes)
    # show the output image
    cv2.imshow('Image', display_image)
    cv2.waitKey(5)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



'''
image = cv2.imread("sample9.jpg")
greyscale_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
decoded_codes = pyzbar.decode(greyscale_image)
display_image = display(decoded_codes,image)
# show the output image
cv2.imshow("Image", display_image)
cv2.waitKey(0)

'''

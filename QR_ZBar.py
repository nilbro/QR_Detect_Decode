import cv2
import pyzbar.pyzbar as pyzbar


def border_display(img, decodedCodes):
    # Loop over all decoded objects
  for decodedObject in decodedCodes:
    points = decodedObject.polygon
    print('Type : ', decodedObject.type)
    print('Data : ', decodedObject.data,'\n')
    #hull = points
    # If the points do not form a quad, find convex hull
    #print(len(points))

    if len(points) > 4 :
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else :
      hull = points;

    # Number of points in the convex hull
    n = len(points)
    # Draw the convext hull
    for j in range(0,n):
      cv2.line(img, hull[j], hull[ (j+1) % n], (0,255,0), 3)
  # Display results
  cv2.imshow("Results", img);
  cv2.waitKey(0);

#read image
image = cv2.imread('sample7.jpg')
#cv2.imshow('QR',image)
#cv2.waitKey(0)
decodedCodes = pyzbar.decode(image)
border_display(image,decodedCodes)

import cv2
img = cv2.imread("noisy.jpg")

imagewithoutnoise = cv2.fastNlMeansDenoisingColored(img, None,20,10,7,21)
cv2.imshow("Detected Edges", imagewithoutnoise)
cv2.waitKey(5000)
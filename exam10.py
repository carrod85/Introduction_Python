import cv2
img = cv2.imread("fight.png")

edge_img = cv2.Canny(img,100,200)
cv2.imshow("Detected Edges", edge_img)
cv2.waitKey(5000)

dimensions = img.shape
print ('dimensions', dimensions)

rotationMatrix = cv2.getRotationMatrix2D(((462) / 2, (693) / 2), 60, .6)
rotatedImage = cv2.warpAffine(img, rotationMatrix, (462, 693))
cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(5000)

imagewithoutnoise = cv2.fastNlMeansDenoisingColored(img, None,10,10,7,21)
cv2.imshow("Detected Edges", imagewithoutnoise)
cv2.waitKey(5000)

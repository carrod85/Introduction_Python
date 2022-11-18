import cv2

img = cv2.imread("sun.jpg")

dimensions = img.shape
print ('dimensions', dimensions)

startRow = int(177*.10)
startCol = int(284*.30)
endRow = int(177*1)
endCol = int(284*.9)
croppedImage=img[startRow:endRow,startCol:endCol]
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', croppedImage)
cv2.waitKey(1000)

rotationMatrix = cv2.getRotationMatrix2D(((endCol-startCol) / 2, (endRow-startRow) / 2), 90, 1)
rotatedImage = cv2.warpAffine(croppedImage, rotationMatrix, ((endCol-startCol), (endRow-startRow)))
cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(5000)


edge_img = cv2.Canny(img,100,200)
cv2.imshow("Detected Edges", edge_img)
cv2.waitKey(5000)
import cv2
img = cv2.imread("/Users/Starkjing/Desktop/ComputerVision/FaceAI/李飞飞.png")

cv2.imshow("Faces found",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

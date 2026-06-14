import cv2
image = cv2.imread("./mountain.jpg")

if image is None:
    print("Not loaded")
else:
    print("Loaded")
    cv2.imshow("mountain", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows
    image_new = image + 30
cv2.imwrite("./output.jpg", image_new)
#Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg", gray)
#Resize Image
resized = cv2.resize(image, (200, 200))
cv2.imwrite("resized.jpg", resized)
#Crop Image
cropped = image[100:400, 100:400]
cv2.imwrite("cropped.jpg", cropped)
#Rotate Image
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imwrite("rotated.jpg", rotated)
#Blur Image
blurred = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite("blurred.jpg", blurred)
#Edge Detection
edges = cv2.Canny(image, 100, 200)
cv2.imwrite("edges.jpg", edges)
#Draw on Image
image_copy = image.copy()
cv2.rectangle(image_copy, (50, 50), (200, 200), (0, 255, 0), 3)
cv2.putText(image_copy, "Mountain", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imwrite("annotated.jpg", image_copy)
#Add Text
text_image = image.copy()
cv2.putText(text_image, "Hello OpenCV", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv2.imwrite("text.jpg", text_image)

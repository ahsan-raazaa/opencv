import cv2

# Reading color image
img = cv2.imread("color-img.png")

# Converting color image to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Showing the converted image
cv2.imshow("Converted Image",gray)

# waiting for key event
cv2.waitKey(0)

# destroying all windows
cv2.destroyAllWindows()

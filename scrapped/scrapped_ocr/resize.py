import cv2
import numpy as np

# Load the two images
img1 = cv2.imread("/home/ubuntu/Vision - Pleasant View Surgery Center (2023-03-10 11-31-46.391).tiff")
img2 = cv2.imread("/home/ubuntu/Vision - Pleasant View Surgery Center (2023-03-13 13-40-46.971).tiff")

shape1 = img1.shape
shape2 = img2.shape

# If the shapes are different, resize the larger image to match the smaller image
if shape1 != shape2:
    if shape1[0] * shape1[1] > shape2[0] * shape2[1]:
        img1 = cv2.resize(img1, (shape2[1], shape2[0]))
    else:
        img2 = cv2.resize(img2, (shape1[1], shape1[0]))

# Save the modified img1 as a new file
cv2.imwrite("/home/ubuntu/new_image1.tiff", img1)
cv2.imwrite("/home/ubuntu/new_image2.tiff", img2)
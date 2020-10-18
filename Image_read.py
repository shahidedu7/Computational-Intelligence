# this is for delete so that it come in fit
import matplotlib.pyplot as plt
image_path = r'C:\Users\Public\Pictures\Sample Pictures\Desert.jpg'   # put your own image path
image = plt.imread(image_path)
plt.imshow(image)


import cv2
image_path = r'C:\Users\Public\Pictures\Sample Pictures\Desert.jpg'
image = cv2.imread(image_path)
plt.imshow(image)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

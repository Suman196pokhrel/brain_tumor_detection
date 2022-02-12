import numpy as np
import PIL
# import matplotlib.pyplot as plt
import cv2

image = r"/mnt/sda2/Final_year_project/btd_final_project/data/no/no0.jpg"

grey_img = cv2.imread(image, 0)
pixel_brightness_transformed  = cv2.convertScaleAbs(grey_img,alpha= 1.2)
threshold , img_threshold = cv2.threshold(grey_img, 110,200, cv2.THRESH_BINARY)
histogram_quilized = cv2.equalizeHist(grey_img)

# Filters 
low_pass_kernel = np.array([
     [1,1,1,1,1],
     [1,1,1,1,1],
     [1,1,1,1,1],
     [1,1,1,1,1],
     [1,1,1,1,1],

]) /25
low_pass_image = cv2.filter2D(grey_img, -1 ,low_pass_kernel)

high_pass_kernel = np.array([
     [-1, -1, -1],
     [-1, 8,-1],
     [-1, -1, -1]
                   ])
high_pass_image = cv2.filter2D(grey_img, -1 ,high_pass_kernel)



cv2.imshow("Greyed Image", grey_img)
cv2.imshow("PBT image", pixel_brightness_transformed)
cv2.imshow("THRESHOLDED image", img_threshold)
cv2.imshow("HIST EQUALIZED image", histogram_quilized)
cv2.imshow("Low pass filter image", low_pass_image)
cv2.imshow("High pass filter image", high_pass_image)




cv2.waitKey(0)
cv2.destroyAllWindows()
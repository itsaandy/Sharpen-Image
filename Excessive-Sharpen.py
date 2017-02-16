import cv2
import numpy as np
import os
import sys

if(len(sys.argv) < 2):
	print "usage python Excessive-Sharpen.py path/to/file"
	sys.exit(-1)

#reading the image
img = cv2.imread(sys.argv[1])

# generating the kernels
kernel_sharpen = np.array([[1,1,1], [1,-7,1], [1,1,1]])


# applying different kernels to the input image
output = cv2.filter2D(img, -1, kernel_sharpen)

newfilenumber = False
i = 0
while(not newfilenumber):
	if(not os.path.isfile("Excessive-Sharpened" + str(i) + ".jpg")):
		cv2.imwrite("Excessive-Sharpened" + str(i) + ".jpg", output)
		newfilenumber = True
	else:
		i+=1

import cv2
import numpy as np
import sys
import os

#Display error message if no command line argument present
if(len(sys.argv) < 2):
    print "Usage: python Sharpen.py path/to/image"
    sys.exit(-1)

#reading the image passed through the command line
img = cv2.imread(sys.argv[1])

# generating the kernels
kernel_sharpen = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])


# applying different kernels to the input image
output = cv2.filter2D(img, -1, kernel_sharpen)

newfilenumber = False
i = 0
while(not newfilenumber):
    if(not os.path.isfile("Sharpened" + str(i) + ".jpg")):
        cv2.imwrite("Sharpened" + str(i) + ".jpg", output)
        newfilenumber = True
    else:
        i+=1

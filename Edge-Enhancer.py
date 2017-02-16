import cv2
import numpy as np
import sys
import os


#displays error message if no command line argument present
if(len(sys.argv) < 2 ):
    print "Usage: python Edge-Enhancer.py path/to/image"
    sys.exit(-1)



#readingt he image passed through the command line
img = cv2.imread(sys.argv[1])

# generating the kernels
kernel_sharpen = np.array([[-1,-1,-1,-1,-1],
                             [-1,2,2,2,-1],
                             [-1,2,8,2,-1],
                             [-1,2,2,2,-1],
                             [-1,-1,-1,-1,-1]]) / 8.0

# applying different kernels to the input image
output = cv2.filter2D(img, -1, kernel_sharpen)

newfilenumber = False
i = 0
while(not newfilenumber):
    if(not os.path.isfile("Edge-Enhanced" + str(i) +".jpg")):
        cv2.imwrite("Edge-Enhanced" + str(i) + ".jpg", output)
        newfilenumber = True
    else:
        i+=1

#  Written by Aditya Pokharel
#  adityapokharel97@gmail.com

import cv2
import numpy as np
import sys


def help_menu():
    print("--Usage--")
    print("NOTE: Press q to quit once image window appears")
    print("Edge Enhancement: ")
    print("   $ python Sharpen.py --edge_enhance /path/to/file")
    print("Sharpen: ")
    print("   $ python Sharpen.py /path/to/file")
    print("Excessive Sharpen: ")
    print("   $ python Sharpen.py --excessive /path/to/file")
    print("Display this menu: ")
    print("   $ python Sharpen.py --help")


def output(img, kernel_sharpen):
    #applying the kernel to the input image
    output = cv2.filter2D(img, -1, kernel_sharpen)


    #displaying the difference in the input vs output
    #quits window if q is pressed
    #switches between the two images when any other key is pressed
    quit = False
    while(not quit):
        cv2.imshow('image', img)
        key = cv2.waitKey(0)
        if(key == ord('q')):
            quit = True
            break;
        cv2.imshow('image', output)
        key = cv2.waitKey(0)
        if(key == ord('q')): #quit the window if q is pressed.
            quit = True
    #Destroys the open window
    cv2.destroyAllWindows()





def sharpen(path):
    #reading the image passed thorugh the command line
    img = cv2.imread(path)

    #generating the kernels
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

    #process and output the image
    output(img, kernel)

def excessive(path):
    #reading the image
    img = cv2.imread(path)

    #generating the kernels
    kernel = np.array([[1,1,1], [1,-7,1], [1,1,1]])

    #process and output the image
    output(img, kernel)

def edge_enhance(path):
    #reading the image
    img = cv2.imread(path)

    #generating the kernels
    kernel = np.array([[-1,-1,-1,-1,-1],
                               [-1,2,2,2,-1],
                               [-1,2,8,2,-1],
                               [-2,2,2,2,-1],
                               [-1,-1,-1,-1,-1]])/8.0

    #process and output the image
    output(img, kernel)




if __name__ == "__main__":
    #Error message if no arguments are passed
    if(len(sys.argv) < 2 or len(sys.argv) > 3):
        help_menu()
        sys.exit(-1)

    #checking the arguments for when 1 argument is passed.
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--help"):
            help_menu()
            sys.exit(-1)
        else:
            sharpen(sys.argv[1])

    #checking the arguments for when 2 arguments are passed.
    elif(len(sys.argv) == 3):
        if(sys.argv[1] == "--sharpen" or sys.argv[2] == "--sharpen"):
            if(sys.argv[1] == "--sharpen"):
                sharpen(sys.argv[2])
            else:
                sharpen(sys.argv[1])

        if(sys.argv[1] == "--excessive" or sys.argv[2] == "--excessive"):
            if(sys.argv[1] == "--excessive"):
                excessive(sys.argv[2])
            else:
                excessive(sys.argv[1])

        if(sys.argv[1] == "--edge_enhance" or sys.argv[2] == "--edge_enhance"):
            if(sys.argv[1] == "--edge_enhance"):
                edge_enhance(sys.argv[2])
            else:
                edge_enhance(sys.argv[1])

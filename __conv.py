import numpy as np
import cv2


#kernel = np.array([[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[-1,-1,-1,-1,-1]])
#kernel = np.array([[1,1,1],[1,0,-1],[-1,-1,-1]])
#kernel = np.array([[1,1,1,1,0],[1,1,1,0,-1],[1,1,0,-1,-1],[1,0,-1,-1,-1],[0,-1,-1,-1,-1]])
#kernel = np.array([[1,1,1,0,0],[1,0,0,0,0],[1,0,0,0,-1],[0,0,0,0,-1],[0,0,-1,-1,-1]])
#kernel = np.array([[1.2,1.2,1.2,0.8,0.8],[1.2,0.8,0.8,0.8,0.8],[1.2,0.8,0.8,0.8,-1.2],[0.8,0.8,0.8,0.8,-1.2],[0.8,0.8,-1.2,-1.2,-1.2]])
#kernel = np.array([[1,1,0.1],[1,0.1,-1],[-1,-1,0.1]])
#kernel = np.array([[0,0,1,0,0],[0,1,-8,1,0],[1,1,0,1,1],[0,1,0,1,0],[0,0,1,0,0]])

#good
#kernel = np.array([[1,1,1],[1,-7,1],[1,1,1]])
#kernel = np.array([[0,1,1,2,2,2,1,1,0],[1,2,4,5,5,5,4,2,1],[1,4,5,3,0,3,5,4,1],[2,5,3,-12,-24,-12,3,5,2],[2,5,0,-24,-40,-24,0,5,2],[2,5,3,-12,-24,-12,3,5,2],[1,4,5,3,0,3,4,4,1],[1,2,4,5,5,5,4,2,1],[0,1,1,2,2,2,1,1,0]])

#image = cv2.imread('./test2.jpg')
# cv2.IMREAD_GRAYSCALE



def conv(kernel, img_path, is_gray):
    if(is_gray):
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    else:  
        img = cv2.imread(img_path)
    
    if img.shape[0] >= kernel.shape[0] and img.shape[1] >= kernel.shape[1]:
        convolved_img = cv2.filter2D(img, -1, kernel)
        write_path = './result/output4.jpg'
        cv2.imwrite(write_path, convolved_img)
        return write_path
    else:
        print("Kernel's size is too small")
        return -1
import numpy as np
import cv2

kernel = [
    np.array([[0,0,0,0,0],[0,-1,0,1,0],[0,0,1,0,0,],[0,-1,0,1,0],[0,0,0,0,0]]),
    np.array([[-1,-2,-1],[-2,13,-2],[-1,-2,-1]]),
    np.array([[-0.5,-1,-0.5],[-1,7,-1],[-0.5,-1,-0.5]]),
    np.array([[0,1,1,2,2,2,1,1,0],[1,2,4,5,5,5,4,2,1],[1,4,5,3,0,3,5,4,1],[2,5,3,-12,-24,-12,3,5,2],[2,5,0,-24,-40,-24,0,5,2],[2,5,3,-12,-24,-12,3,5,2],[1,4,5,3,0,3,4,4,1],[1,2,4,5,5,5,4,2,1],[0,1,1,2,2,2,1,1,0]]),
    np.array([[1/81 for i in range(9)] for j in range(9)]),
    np.array([[1,1,1],[1,-7,1],[1,1,1]]),
    np.array([[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[-1,-1,-1,-1,-1]]),
    np.array([[2,0,0],[0,1,0],[0,0,-2]]),
    np.array([[-0.5,-1,-1.5,-1,-0.5],[-1,-1.5,-2,-1.5,-1],[-1.5,-2,31,-2,-1.5],[-1,-1.5,-2,-1.5,-1],[-0.5,-1,-1.5,-1,-0.5]]),
    np.array([[0.003,0.013,0.022,0.013,0.003],[0.013,0.060,0.098,0.060,0.013],[0.060,0.098,0.162,0.098,0.060],[0.013,0.060,0.098,0.060,0.013],[0.003,0.013,0.022,0.013,0.003]]),
]

for i in range(10):
    image_path = './input/' + str(i+1) + '.png'
    image = cv2.imread(image_path)
    output_image = cv2.filter2D(image, -1, kernel[0])
    output_path = './output/' + str(i+1) + '.png'
    cv2.imwrite(output_path,output_image)
import numpy as np
import cv2
import ctypes

cap = cv2.VideoCapture(0) # this is the magic!

cv2.namedWindow("Camera", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

kernel = [
    np.array([[0,1,1,2,2,2,1,1,0],[1,2,4,5,5,5,4,2,1],[1,4,5,3,0,3,5,4,1],[2,5,3,-12,-24,-12,3,5,2],[2,5,0,-24,-40,-24,0,5,2],[2,5,3,-12,-24,-12,3,5,2],[1,4,5,3,0,3,4,4,1],[1,2,4,5,5,5,4,2,1],[0,1,1,2,2,2,1,1,0]]),
    np.array([[1,1,1],[1,-7,1],[1,1,1]]),
    np.array([[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[-1,-1,-1,-1,-1]]),
    np.array([[2,0,0],[0,1,0],[0,0,-2]])
]

kernel_num = 0
timer = 0

user32 = ctypes.windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


mask = np.array([[[225,225,225] for i in range(screen_width-300)] for j in range(screen_height)], dtype=float)
output_image = np.zeros((screen_height,screen_width,3))


while(True):

 
 # read video frame by frame
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    frame_height, frame_width, _ = frame.shape

    scaleWidth = float(screen_width)/float(frame_width)
    scaleHeight = float(screen_height)/float(frame_height)

    imgScale=min(scaleHeight,scaleWidth)

    newX,newY = frame.shape[1]*imgScale, frame.shape[0]*imgScale
    frame = cv2.resize(frame,(int(newX),int(newY)))


    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    if frame.shape[0] >= kernel[kernel_num].shape[0] and frame.shape[1] >= kernel[kernel_num].shape[1]:
        convolved_image = cv2.filter2D(frame, -1, kernel[kernel_num])
    else:
        print("Kernel's size is too small")
    
    output_image[0:int(screen_height), 0:int(screen_width-300)] = mask
    output_image[0:int(newY), 0:int(newX)] = convolved_image
    '''
    for i,a in zip(convolved_image, output_image[0:int(newY), 0:int(newX)]) :
        for j,b in zip(i,a):
            for k,c in zip(j,b):
                print(k-c)
    '''
    cv2.imshow('live2', convolved_image)
    #cv2.imshow('live', gray)
    cv2.imshow('live',output_image)

    if cv2.waitKey(1) == ord('q'):
        break

    timer+=1
    if timer>150:
        timer = 0
        kernel_num = (kernel_num+1)%len(kernel)

cap.release()
cv2.destroyAllWindows()

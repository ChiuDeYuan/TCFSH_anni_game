import numpy as np
import cv2
import ctypes

cap = cv2.VideoCapture(0) # this is the magic!

cv2.namedWindow("Camera", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

if not cap.isOpened():
    print("Cannot open camera")
    exit()


kernel1 = np.array([[0,1,1,2,2,2,1,1,0],[1,2,4,5,5,5,4,2,1],[1,4,5,3,0,3,5,4,1],[2,5,3,-12,-24,-12,3,5,2],[2,5,0,-24,-40,-24,0,5,2],[2,5,3,-12,-24,-12,3,5,2],[1,4,5,3,0,3,4,4,1],[1,2,4,5,5,5,4,2,1],[0,1,1,2,2,2,1,1,0]])
#kernel1 = np.array([[1,1,1],[1,-7,1],[1,1,1]])
#kernel1 = np.array([[1]])

#kernel1 = np.array([[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[-1,-1,-1,-1,-1]])
# cv2.IMREAD_GRAYSCALE

while(True):

    user32 = ctypes.windll.user32
    screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
 
 # read video frame by frame
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    frame_height, frame_width, _ = frame.shape

    scaleWidth = float(screen_width)/float(frame_width)
    scaleHeight = float(screen_height)/float(frame_height)

    if scaleHeight>scaleWidth:
        imgScale = scaleWidth

    else:
        imgScale = scaleHeight

    newX,newY = frame.shape[1]*imgScale, frame.shape[0]*imgScale
    frame = cv2.resize(frame,(int(newX),int(newY)))

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    if frame.shape[0] >= kernel1.shape[0] and frame.shape[1] >= kernel1.shape[1]:
        convolved_image1 = cv2.filter2D(frame, -1, kernel1)
    else:
        print("Kernel's size is too small")
    
    cv2.imshow('live', convolved_image1)
    #cv2.imshow('live', gray)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
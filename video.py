import cv2 as cv
def display():
    cap = cv.VideoCapture(0)
    while True:
        ret,frame =cap.read()
        cv.imshow('Live Web-Cam',frame)
        key = cv.waitKey(1)
        if key in [28,91,100]:
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__' :
    display()

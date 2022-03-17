import cv2


def dispImg():
    img=cv2.imread('data/lena.jpg',0)
    cv2.imshow('image',img)
    #binding events
    k=cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
    else:
        cv2.imwrite('data/copy/lena_copy.jpg',img)
        cv2.destroyAllWindows()
# hello just testing
def captureVideo():
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    while (cap.isOpened()):
        ret, frame = cap.read()        
        cv2.imshow('frame',frame)
        #k=cv2.waitKey(1) & 0xFF
        if cv2.waitKey(1) & 0xFF==27:
            break

    cap.release()
    cv2.destroyAllWindows()

captureVideo()
#def main():
#    dispImg()
#    captureVideo()

#main()
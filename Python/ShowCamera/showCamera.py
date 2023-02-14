import cv2
import time


def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    while True:
        ret_val, img = cam.read()
        #img=cv2.resize(img,(1910,1070),interpolation = cv2.INTER_NEAREST)
        cv2.imshow('ps4', img)
        time.sleep(0.001)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()

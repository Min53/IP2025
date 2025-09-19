import cv2
import numpy as np

drawing = False
ix, iy = -1, -1
current_x, current_y = -1, -1
img = None
img_clean = None

def nothing(x):
    pass

def mouse_handler(event, x, y, flags, param):
    global ix, iy, drawing, img, current_x, current_y

    current_x, current_y = x, y

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x1, y1 = min(ix, x), min(iy, y)
        x2, y2 = max(ix, x), max(iy, y)

        if x1 < x2 and y1 < y2:
            temp_overlay = img.copy()
            cv2.rectangle(temp_overlay, (x1, y1), (x2, y2), (0, 0, 255), -1)
            img = cv2.addWeighted(temp_overlay, 0.4, img, 0.6, 0)

img = cv2.imread('ararat.jpg')
if img is None:
    exit()

img_clean = img.copy()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 1280, 720)
cv2.setMouseCallback('image', mouse_handler)

cv2.createTrackbar('value', 'image', 0, 100, nothing)

while True:
    display_img = img.copy()

    if drawing:
        cv2.rectangle(display_img, (ix, iy), (current_x, current_y), (0, 0, 255), -1)
        display_img = cv2.addWeighted(display_img, 0.4, img.copy(), 0.6, 0)

    font = cv2.FONT_HERSHEY_SIMPLEX
    value = cv2.getTrackbarPos('value', 'image')
    
    text = f"Mouse position ({current_x},{current_y}) - ({ix},{iy}) - {value} - 0 - 3"
    
    cv2.putText(display_img, text, (10, 20), font, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow('image', display_img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('c'):
        img = img_clean.copy()
        ix, iy = -1, -1

cv2.destroyAllWindows()
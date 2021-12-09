import  cv2
import  pytesseract
import  numpy as np

pytesseract.pytesseract.tesseract_cmd = 'tesseract'

img =  cv2.imread("img/IMG_5105.PNG")

hImg, wImg, zImg = img.shape
boxes = pytesseract.image_to_data(img)

for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        #print(b)
        """ x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 1)
        cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2) """

cv2.imshow('Image Window', img)
cv2.waitKey(0)
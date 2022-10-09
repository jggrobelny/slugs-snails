import cv2
import numpy as np
import uuid


def run(filename):
    def recognition(cascade_, name, color, img):
        cascades = cascade_.detectMultiScale(imgray, scaleFactor=3, minNeighbors=3)
        for (x, y, w, h) in cascades:
            roi_gray = imgray[y:y + h, x:x + w]
            stroke = 2
            width = x + w
            height = y + h
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(img, (x, y), (end_cord_x, end_cord_y), color, stroke)  # wyswietlanie ramki

            # tekst
            label = name
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (end_cord_x, end_cord_y)
            fontScale = 1
            color_font = color
            thickness = 2

            img = cv2.putText(img, label, org, font, fontScale, color_font, thickness, cv2.LINE_AA)

            return img
        return img

    cascade1_ = cv2.CascadeClassifier('b_cascade.xml')
    color1 = (255, 0, 0)
    name1 = "blotniarka"

    cascade2_ = cv2.CascadeClassifier('w_cascade.xml')
    color2 = (0, 255, 0)
    name2 = "winniczek"

    cascade3_ = cv2.CascadeClassifier('h_cascade.xml')
    color3 = (0, 0, 255)
    name3 = "helenka"

    img = cv2.imread(filename)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # nakładanie na obraz poszczególnych ramek i etykiet w wypadku wykrycia gatunku
    img = recognition(cascade1_, name1, color1, img)
    img = recognition(cascade2_, name2, color2, img)
    img = recognition(cascade3_, name3, color3, img)


    dim = (img.shape[1], img.shape[0])
    output = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    path_img = str(uuid.uuid1()) + ".jpg"
    cv2.imwrite(path_img, output)



    return path_img

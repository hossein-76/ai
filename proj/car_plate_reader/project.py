import cv2
import random


inF = open('lastIndex.txt', 'r')
counter = int(inF.read())
inF.close()
fileNumber = int(input('file number: '))
for i in range(fileNumber):
    img = cv2.imread('./plates/plate' + str(i + 1) + '.jpg', 0)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite("BlackWhite.jpg", th3)
    img = cv2.imread('BlackWhite.jpg')
    height, width, depth = img.shape
    minValidHeght = height * 0.5
    minValidWidth = width * 0.1
    maxValidHeght = height * 0.7
    maxValidWidth = width * 0.4
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)
    thresh_color = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    thresh = cv2.dilate(thresh, None, iterations=3)
    thresh = cv2.erode(thresh, None, iterations=2)
    a, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    lst = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        found = False
        if (w > minValidWidth or h > minValidHeght) and w < h < maxValidHeght and w < maxValidWidth:
            # print x,y,w,h
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            for l in lst:
                if l[0] > x and l[2] < w and l[0] + l[2] < x + w and l[1] > y and l[3] < h and l[1] + l[3] < y + h:
                    l[0] = x
                    l[1] = y
                    l[2] = w
                    l[3] = h
                    found = True
                    break
            if not found:
                lst.append([x, y, w, h])
    for l in lst:
        x, y, w, h = l
        crop_img = img[y:y + h, x:x + w]
        cv2.imwrite(str(counter) + ".jpg", crop_img)
        counter += 1
outF = open('lastIndex.txt', 'w')
outF.write(str(counter))
outF.close()

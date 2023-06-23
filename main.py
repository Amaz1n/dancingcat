# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2 as cv
import sys


def draw(images):
    i = 0
    j = 1
    cv.imshow("danc cat", images[0])
    while cv.getWindowProperty("danc cat", 0) >= 0:
        cv.imshow("danc cat", images[i])
        i += j

        if (i <= 0 and j == -1) or (i >= len(images) - 1 and j == 1):
            j *= -1

        cv.waitKey(200)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img_list = []

    for i in range(3):
        img = cv.imread(cv.samples.findFile("cat" + str(i+1) + ".jpg"))

        if img is not None:
            img_list.append(img)

    draw(img_list)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Cat doing a silly dance

import cv2


# Draw the frames
def draw(images):
    i = 0
    j = 1
    cv2.imshow("danc cat", images[0])
    while True:
        cv2.imshow("danc cat", images[i])
        i += j

        if (i <= 0 and j == -1) or (i >= len(images) - 1 and j == 1):
            j *= -1

        cv2.waitKey(200)

        if cv2.getWindowProperty("danc cat", cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()


# Main program code
if __name__ == '__main__':
    img_list = []

    for i in range(3):
        img = cv2.imread(cv2.samples.findFile("cat" + str(i+1) + ".jpg"))

        if img is not None:
            img_list.append(img)

    draw(img_list)

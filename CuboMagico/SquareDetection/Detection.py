import cv2  # self explain

image = cv2.imread("shapes.png")  # say to the computer read the img in the address

gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # transform de image in a gray scale

_, thresh_img = cv2.threshold(gray_scale, 220, 255, cv2.THRESH_BINARY)  # if pixel value <= 220: black; else: white

contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# find the contours and save only the corners

for i, contour in enumerate(contours):
    if i == 0:  # ignore the first contour
        continue

    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    # this line and the previous make the cv2 read imperfections, the True say that they are closed shapes

    cv2.drawContours(image, contour, 0, (0, 255, 0), 4)

    x, y, w, h = cv2.boundingRect(approx)  # find the coordinates of the shapes
    x_mid = int(x + (w / 3))  # returns the center of the x
    y_mid = int(y + (w / 1.5))  # returns the center of the y
    # originally the 3 and the 1.5 where both 2, but the text was a little bit dislocate, so it's 3 and 1.5
    # they don't make any difference

    cords = (x_mid, y_mid)
    colour = (0, 0, 0)
    font = cv2.FONT_HERSHEY_DUPLEX

    if len(approx) == 3:
        cv2.putText(image, "Triangle", cords, font, 1, colour, 1)  # Text on the image
    elif len(approx) == 4:
        cv2.putText(image, "Quadrilateral", cords, font, 1, colour, 1)
    elif len(approx) == 5:
        cv2.putText(image, "Pentagon", cords, font, 1, colour, 1)
    elif len(approx) == 6:
        cv2.putText(image, "Hexagon", cords, font, 1, colour, 1)
    else:
        # If the length is not any of the above, we will guess the shape/contour to be a circle.
        cv2.putText(image, "Circle", cords, font, 1, colour, 1)

cv2.imshow("Images", image)
cv2.waitKey(0)

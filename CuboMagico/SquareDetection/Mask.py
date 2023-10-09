import cv2
import numpy as np

low_ = np.array([200, 100, 200])
high_ = np.array([200, 200, 200])

cap = cv2.imread("Shapes.png")

B, G, R = cap[100, 100]
print(R, G, B)
cv2.circle(cap, (100, 100), 1, (0, 255, 0))


while True:
    cv2.imshow("Original", cap)

    hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv)

    mask = cv2.inRange(hsv, low_, high_)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

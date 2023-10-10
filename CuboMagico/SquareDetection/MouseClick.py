import cv2


def mouse_click(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(cap, (x, y), 10, (0, 0, 255), -1)


cap = cv2.imread("img.png")

while True:
    cv2.imshow("Original", cap)
    cv2.setMouseCallback('Original', mouse_click)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# importing the module
import cv2
import matplotlib.pyplot as plot

i = 1
x_co = []
y_co = []
dist = []


# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    global i
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        x_co.append(x)
        y_co.append(y)
        dist.append(((x_co[0] - x_co[len(x_co) - 1]) ** 2 + (y_co[0] - y_co[len(y_co) - 1]) ** 2) ** 0.5)
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(i), (x, y), font,
                    0.5, (255, 255, 255), 1)

        cv2.imshow('image', img)
        if i == 500:
            drawPlot()
            return
        i += 1
    # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        # b = img[y, x, 0]
        # g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(i) + ',' + str(r),
                    (x, y), font, 0.5,
                    (255, 255, 0), 1)
        i += 1
        cv2.imshow('image', img)


def drawPlot():
    x_values = [x_co[0], x_co[len(x_co) - 1]]
    y_values = [y_co[0], y_co[len(y_co) - 1]]
    dist.sort()
    maxDist = dist[len(dist) - 1]
    print(maxDist)
    plot.plot(x_values, y_values, color="black", linestyle='-')
    plot.title("Distance Graph(Max Distance is the length of this plot calculated by the coordinates)")
    plot.xlabel("X Values")
    plot.ylabel("Y Values")
    plot.show()


# driver function
if __name__ == "__main__":
    # reading the image
    img = cv2.imread('wallpaper2.jpg', 1)

    # displaying the image
    cv2.imshow("image", img)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
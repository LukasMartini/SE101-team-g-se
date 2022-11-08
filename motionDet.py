import cv2 as cv
import numpy
import numpy as np
import frames

def motionDet(oldFrame, newFrame, oldPoint, lkPresets):
    moveStatus = 0 # a checker for if there is movement.
    color = np.random.randint(0, 255, (100, 3)) # Picks random colors. This is only for if there are things being drawn and should be deleted later.
    ofGrey = cv.cvtColor(oldFrame, cv.COLOR_BGR2GRAY) # sets the input frames to greyscale if they weren't already.
    nfGrey = cv.cvtColor(newFrame, cv.COLOR_BGR2GRAY)
    newPoint, status, error = cv.calcOpticalFlowPyrLK(ofGrey, nfGrey, oldPoint, None, lkPresets) # calculates the new optical flow points.

    if newPoint is not None: # takes the array of points returned by calcOpticalFlowPyrLK and only keeps the ones where the status is true (i.e the "best" points)
        good_new = newPoint[status==1]
        good_old = oldPoint[status==1]


    for i, (new, old) in enumerate(zip(good_new, good_old)): # flattens the array of points for both the new and old frames.
        a, b = new.ravel()
        c, d = old.ravel()

        if (abs(a - c) > 0.1) and (abs(b - d) > 0.1): # checks to see if the difference between the old and new frame is great enough to constitute "movement"
            moveStatus = 1

        #drawing code
        mask = cv.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
        frame = cv.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
    #additionall drawing code
    img = cv.add(frame, mask)
    cv.imshow('frame', img)

    oldPoint = good_new.reshape(-1, 1, 2) # does some array magic
    return newFrame, oldPoint, moveStatus # returns the values used in the next iteration

class motionDet(frames.ModelClass):
    def __init__(self, frame: numpy.ndarray):
        oldFrame = frame

    def motionDet(oldFrame, newFrame, oldPoint, lkPresets):
        moveStatus = 0  # a checker for if there is movement.
        color = np.random.randint(0, 255, (
        100, 3))  # Picks random colors. This is only for if there are things being drawn and should be deleted later.
        ofGrey = cv.cvtColor(oldFrame, cv.COLOR_BGR2GRAY)  # sets the input frames to greyscale if they weren't already.
        nfGrey = cv.cvtColor(newFrame, cv.COLOR_BGR2GRAY)
        newPoint, status, error = cv.calcOpticalFlowPyrLK(ofGrey, nfGrey, oldPoint, None,
                                                          lkPresets)  # calculates the new optical flow points.

        if newPoint is not None:  # takes the array of points returned by calcOpticalFlowPyrLK and only keeps the ones where the status is true (i.e the "best" points)
            good_new = newPoint[status == 1]
            good_old = oldPoint[status == 1]

        for i, (new, old) in enumerate(
                zip(good_new, good_old)):  # flattens the array of points for both the new and old frames.
            a, b = new.ravel()
            c, d = old.ravel()

            if (abs(a - c) > 0.1) and (
                    abs(b - d) > 0.1):  # checks to see if the difference between the old and new frame is great enough to constitute "movement"
                moveStatus = 1

            # drawing code
            mask = cv.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
            frame = cv.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
        # additionall drawing code
        img = cv.add(frame, mask)
        cv.imshow('frame', img)

        oldPoint = good_new.reshape(-1, 1, 2)  # does some array magic
        return newFrame, oldPoint, moveStatus  # returns the values used in the next iteration

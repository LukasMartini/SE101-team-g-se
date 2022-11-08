import cv2 as cv
import numpy
import numpy as np
import frames

class motionDet(frames.ModelClass):
    def __init__(self, frame: numpy.ndarray): # Sets constants and presets used in every iteration as well as the original frame used as a basis.
        self.oldFrame = frame # Basis frame.
        self.ShiTomasiPresets = dict(maxCorners=100, qualityLevel=0.1, minDistance=7, blockSize=7) # Edge detection presets.
        self.LukasKanadePresets = dict(winSize=(5, 5), maxLevel=2, criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03)) # Optical flow presets
        self.ofGrey = cv.cvtColor(self.oldFrame, cv.COLOR_BGR2GRAY)  # Makes the frame greyscale
        self.oldPoint = cv.goodFeaturesToTrack(self.ofGrey, mask=None, ** self.ShiTomasiPresets) # Creates a basis point map for the first round of edge detection.


    def process(self, newFrame):
        moveStatus = 0  # a checker for if there is movement.
        color = np.random.randint(0, 255, (100, 3))  # Picks random colors. This is only for if there are things being drawn and should be deleted later.
        ofGrey = cv.cvtColor(self.oldFrame, cv.COLOR_BGR2GRAY)  # sets the input frames to greyscale if they weren't already.
        nfGrey = cv.cvtColor(self.newFrame, cv.COLOR_BGR2GRAY)
        newPoint, status, error = cv.calcOpticalFlowPyrLK(ofGrey, nfGrey, self.oldPoint, None,
                                                          self.LukasKanadePresets)  # calculates the new optical flow points.

        if newPoint is not None:  # takes the array of points returned by calcOpticalFlowPyrLK and only keeps the ones where the status is true (i.e the "best" points)
            good_new = newPoint[status == 1]
            good_old = self.oldPoint[status == 1]

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

        self.oldPoint = good_new.reshape(-1, 1, 2)  # does some array magic
        self.oldFrame = newFrame # Passes on the frame so that it can be checked against the new incoming frame.
        self.oldPoint = cv.goodFeaturesToTrack(self.nfGrey, mask=None, ** self.ShiTomasiPresets) # Updates the edge detection

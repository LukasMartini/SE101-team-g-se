import cv2 as cv
import modularMotionDet # May need to be done differently in the git itself

#needs:
# function that returns a given frame
# have a main function that permanently runs the camera on it's own

# credit: https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html NOTE: this is my code, but it borrows heavily from the ideas of the tutorial, hence the credit

def permRunCam():

    #Important presets:

    # Parameters for the Shi-Tomasi corner detection algorithm
    ShiTomasiPresets = dict(maxCorners=100, qualityLevel=0.1, minDistance=7, blockSize=7)
    # Parameters for lucas kanade optical flow
    LukasKanadePresets = dict(winSize=(5, 5), maxLevel=2, criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))


    feed = cv.VideoCapture(0)
    oldFrame = feed.read() # pulls the first frame as a basis
    ofGrey = cv.cvtColor(oldFrame, cv.COLOR_BGR2GRAY) # makes the frame greyscale
    oldPoint = cv.goodFeaturesToTrack(ofGrey, mask=None **ShiTomasiPresets) ## keep in mind that this may need to be done in each loop to avoid some kind of point decay. TEST THIS LATER.
    while (1):
        frame = feed.read() ## reads the next frame.
        newFrame, oldPoint, moveStat = modularMotionDet(oldFrame, frame, oldPoint, LukasKanadePresets) # Runs regular motion det.
        if moveStat == 1:
            print("hello")
        oldFrame = newFrame ## resets frames.
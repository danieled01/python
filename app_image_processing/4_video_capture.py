#we are now going to use cv2 to do some video capturing - which are essentially many images being opened in a loop

import cv2

#We are going to use the VideoCapture() method to open up the built in camera as thats what 0 points to.  If you were going to process a video file you would pass the file name as a an argument to the method like we did for the DDR picture.
video=cv2.VideoCapture(0)

#in order to get the video to show the images continously we will make our program run in a loop so it will display the image continously thus making a video.
while True:
#Here is a neat little trick where we use check to see if the video is running but we also map frame variable to video.read() which is what we are capturing with our built in camera
    check, frame=video.read()
    cv2.imshow("video",frame)
    cv2.waitKey(1)
    if cv2.waitKey(1)==ord('a'):
        break

#this releases the lock on the camera
video.release()
cv2.destroyAllWindows

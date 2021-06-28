#We are going to build a an app that detects moving objects using a webcam - this is a follow on from what we have covered in app_image_processin.
#How the program operates is as follows:
#   - On the first run the script will take a picture which it will use as a baseline - this will be static picture which will be used by the script to compare the subequent pictures to and detect changes.
#   - We will then convert the background image to gray scale as that will improve accuracy when detecting chnages.
#   - Then you will apply the same method to the subsequent pictures taken in the loop (so take the picture then gray them out).
#   - The script will then compare the grayed baseline image and the grayed out subsequent images and detect changes.
#   - We will then apply some logc where we tell the script that if there is a density greater than 100 to turn those pixels to white and pixels below to black.  this will provide with the silhoutte of the object that has moved within the camera frame.
#   - Then within our while loop we will map out the contours of the white pixeled areas and set up some logic that discards white pixeled areas which are smaller than a certain threshold therefore not likely to be the object that we are looking to capture (for exmaple an animal or a person).
#   - The script will also use the contours and draw a rectangle around the image, much like we did for processing faces on pictures.

import cv2, time

#Start off by mapping a variable to the VideoCapture(0) method of cv2 which grabs a stream from our builtin cam.  As we have seen the video is just a series of pictures so what we capture here is then streamed via the .read(), .imshow() and .waitKey(1) specified in the while loop.
video=cv2.VideoCapture(0)

#In order to create our baseline dataframe we declare a variable outside the while loop and map it to None.  We will then create an if statement that maps an object to the variable when the script first runs.
baseline_frame=None

#while loop to continously process the images as a stream.
while True:

    check, frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#Once we have taken the first frame we will apply a gaussion blur which removes noise and improves accuracy (21,21),0 are commonly used numbers for the deviation of the blurriness.
    gray=cv2.GaussianBlur(gray,(21,21),0)

#This is where we pick up the baseline_frame and state that if it is set to None then map the first picture to it, when the loop runs through again it checks it and sees #that baseline_frame has a value therefore ignores the conditional.  The continue instruction tells python not to execute the lines below and just start the loop again.
    if baseline_frame is None:
        baseline_frame=gray
        continue

#We now work out the differences between the baseline frame and the subsequent frames taken in the loop.
    differences=cv2.absdiff(baseline_frame,gray)

#Now that we have the baseline frame and the subsequent frames we are going to either white or blackout pixels based on the difference of the values. we also smooth it out
    convert_differences=cv2.threshold(differences,20,255, cv2.THRESH_BINARY)[1]
    convert_differences=cv2.dilate(convert_differences,None,iterations=2)

#This block of code is how we find the contours and assign to the (__,cnts__) - we also iterate through each contor and draw lines around it based on the area size.
    (__,cnts,__)=cv2.findContours(convert_differences.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(gray, (x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("contour",gray)
    cv2.imshow("diff",differences)
    cv2.imshow("convert",convert_differences)
#the next 2 lines of code are a follow on to lines 22/23 were the video variable and stream the video on a loop ever 1ms.
    cv2.imshow("video",gray)
    cv2.waitKey(1)

#the conditional below states that if we press the q the loop is broken which means the script runs the video.release() and cv2 destroyAllWindows.
    if cv2.waitKey(1)==ord('q'):
        break

video.release()
cv2.destroyAllWindows

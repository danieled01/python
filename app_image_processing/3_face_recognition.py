#in order to be able to detect faces on images we will use haarcascade files which come as xml files downloadable from github.  These contain the data required in order to detect the different pixels in an image required to detect faces.
import cv2

#CascadeClassifier() method used to map the haarcascade_frontalface_default xml so we can use that later in our script.
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#load our image as grayscale as that is better for accuracy
img=cv2.imread("ddr.jpg",1)
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#now we will look for the face on the picture - the scaleFactor=1.05 tells python to scan for the face features in the xml file on the same size picture to being with, then it looks for smaller faces by decreasing the picture by 5% each time.  If you chose 1.01 it will do it by 1%.
faces=face_cascade.detectMultiScale(grey_img,scaleFactor=1.05,minNeighbors=5)

#Here we run a print just to see the type of the obejct and the values in the objectl
print(faces)
print(type(faces))

#so faces becomes a numpy array with 4 items in the list which represent the starting point of the top left hand corner of the face and the length in pixels for the x and y axis that will dictate the length of the left and top side which get calculated with (x+w,y+h). These are the parameters that you set to the color and line size of the rectangle around the face (0,255,0),3)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow('DDR',img)
cv2.waitKey(20000)
cv2.destroyAllWindows()

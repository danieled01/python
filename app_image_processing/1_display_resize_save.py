#The library used for image mgmnt is cv2.
import cv2

#In order to open the image you need to map it to a variable and open it using the imread() method.  You will then use another argument for the colours so:
#   - 1  - colours
#   - 0  - Black and White
#   = -1 - Transparent
img=cv2.imread("ddr.jpg",0)


#what cv2 does is load the image into python as a numpy array with lists that are made up of all the pixels that make up the image.  For example:

#print(type(img))
#img=cv2.imread("ddr.jpg",1)
#print(type(img))
#img=cv2.imread("ddr.jpg",-1)
#print(type(img))


#The shape method will show you the picture dimension
print(img.shape)

#the ndim method will show you how many dimension the image has - so for -1 and 1 will be 3 and 0 will be 2.
print(img.ndim)

#You are also able to resize a picture using the resize() method
resized_img=cv2.resize(img,(1000,500))

#You can then save the image
cv2.imwrite("ddr_resized.jpg",resized_img)

#the imshow() method will open the window with your picture and then waitKey() method will dictate how long to keep the window up before closing it by making use of the destroyAllWindows() method.
cv2.imshow("DDR", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

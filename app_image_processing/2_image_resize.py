import glob, os, cv2

os.chdir("sample-images")

for item in glob.glob("*.jpg"):
    img=cv2.imread(item,1)
    resized_img=(cv2.resize(img,(100,100)))
    cv2.imwrite(item+'_resized.jpg',resized_img)
    cv2.imshow(item,resized_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

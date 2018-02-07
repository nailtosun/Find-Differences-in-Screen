from PIL import ImageChops,ImageGrab,Image
def mymain():
    for i in range(1,10):
        if i%2:
            snapshot = ImageGrab.grab() #takes screenshot
            image1 = "C:\\screenshot1.jpg"
            snapshot.save(save_path1)
        else:
            snapshot = ImageGrab.grab()
            image2 = "C:\\screenshot2.jpg"
            snapshot.save(save_path2)
            im1 = Image.open("C:\\screenshot1.jpg")
            im2 = Image.open("C:\\screenshot2.jpg")
            diff = ImageChops.difference(im1,im2).getbbox()
            print (diff)
        if i==10:
            mymain() #recursive call for infinite loop
mymain()

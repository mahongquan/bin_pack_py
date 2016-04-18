# -*- coding:Utf-8 -*-
from PIL import Image,ImageDraw
import random
if __name__=="__main__":
    for i in range(30):
        (w1,h1)=(random.randint(10,100), random.randint(10,100))
        (r,g,b)=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        im=Image.new("RGBA",(w1,h1))
        w =ImageDraw.ImageDraw(im) #Canvas(master, width=pack.root.w, height=pack.root.h)
        w.rectangle((0,0,w1,h1),(r,g,b))
        w.text((0,10),text=str(i))
        im.save("test/%d.png" % i)

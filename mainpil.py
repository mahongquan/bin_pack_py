# -*- coding:Utf-8 -*-
from PIL import Image,ImageDraw
print(dir())
from main import demo
if __name__=="__main__":
    (pack,blocks)=demo()
    im=Image.new("RGBA",(pack.root.w, pack.root.h))
    w =ImageDraw.ImageDraw(im) #Canvas(master, width=pack.root.w, height=pack.root.h)
    # #print(dir(w))
    # w.configure(background='black')
    # w.bind("<Motion>", showxy)
    # w.pack()
    for n in range(len(blocks)):
        block = blocks[n];
        if (block.fit):
          #print(block.fit.x, block.fit.y, block.w, block.h,block.used)
          w.rectangle((block.fit.x, block.fit.y,block.fit.x+block.w, block.fit.y+block.h),fill="green", outline="black")
          w.text((block.fit.x,block.fit.y+10),text=str(n))
    im.save("out.png")

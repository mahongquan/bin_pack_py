#!/usr/bin/python3
# -*- coding:Utf-8 -*-
from pprint import pprint
from tkinter import *
from main import demo
#w.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill="red", outline="black")
if __name__=="__main__":
    (pack,blocks)=demo()
    def showxy(event):
        xm, ym = event.x, event.y
        str1 = "mouse at x=%d  y=%d" % (xm, ym)
        # show cordinates in title
        master.title(str1)

    master = Tk()
    w = Canvas(master, width=pack.root.w, height=pack.root.h)
    #print(dir(w))
    w.configure(background='black')
    w.bind("<Motion>", showxy)
    w.pack()
    for n in range(len(blocks)):
        block = blocks[n];
        if (block.fit):
          #print(block.fit.x, block.fit.y, block.w, block.h,block.used)
          w.create_rectangle(block.fit.x, block.fit.y,block.fit.x+block.w, block.fit.y+block.h, fill="green", outline="black")
          w.create_text((block.fit.x+10,block.fit.y+10),text=str(n))
    mainloop()
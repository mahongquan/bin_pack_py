import getfiles
from packer import *
import random
import functools
from PIL import Image
def flip(o1):
    if o1.h<o1.w:
        o1.rotate=True
        tmp=o1.h
        o1.h=o1.w
        o1.w=tmp
def comp(o1,o2):
    flip(o1)
    flip(o2)
    if o1.h<o2.h:
        return 1
    elif o1.h>o2.h:
        return -1
    else:
        if o1.w<o2.w:
            return 1
        elif o1.w>o2.w:
            return -1
        else:
            return 0
def demo():
    packer = Packer(256,512)  # or:  new GrowingPacker();
    files=getfiles.getfiles()
    nodes=[]
    for f in files:
        im=Image.open(f)
        node=Node(im.size[0],im.size[1])
        node.filename=f
        nodes.append(node)
    nodes=sorted(nodes,key=functools.cmp_to_key(comp))
    packer.fit(nodes);
    im=Image.new("RGBA",(packer.root.w,packer.root.h))
    for n in range(len(nodes)):
        block = nodes[n];
        if (block.fit!=None):
          print(n,block.fit.x, block.fit.y, block.w, block.h,block.fit.used,block.filename,block.rotate)
          im1=Image.open(block.filename)
          if block.rotate==True:
            im1=im1.rotate(-90)
          im.paste(im1,(block.fit.x, block.fit.y))
        else:
          print(n,block.x, block.y, block.w, block.h,block.used,block.filename,block.rotate)
    print(packer.root.w,packer.root.h)
    im.save("output.png")
    return(packer,nodes)
if __name__=="__main__":
    demo()
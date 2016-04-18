from packer import *
import random
import functools
#import Image
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
    #packer = GrowingPacker(256, 512)  # or:  new GrowingPacker();
    nodes=[]
    for i in range(30):
        node=Node(random.randint(10,100),random.randint(10,100))
        nodes.append(node)
    # nodes = [
       # Node(100,100),Node(100,100),Node(80,80),Node(80,80) ]
    # i=0
    # while i < 2 :
        # nodes.append(Node(90, 230))
        # i += 1
    # i = 0
    # while i < 10 :
        # block = Node(115, 166)
        # #if i in [0,1,2,3]:
        # #    block.flip()
        # nodes.append(block)
        # i += 1
    # i = 0
    # while i < 0 :
        # nodes.append(Node(186, 129))
        # i += 1

    #mysort(nodes)#.sort()#function(a,b) { return (b.h < a.h); }); // sort inputs for best results
    #nodes.sort(key=lambda var:var.h*var.w, reverse=True)
    nodes=sorted(nodes,key=functools.cmp_to_key(comp))
    packer.fit(nodes);
    for n in range(len(nodes)):
        block = nodes[n];
        if (block.fit!=None):
          print(n,block.fit.x, block.fit.y, block.w, block.h,block.fit.used)
        else:
          print(n,block.x, block.y, block.w, block.h,block.used)
    print(packer.root.w,packer.root.h)
    return(packer,nodes)
if __name__=="__main__":
    demo()
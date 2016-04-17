from packer import *
import random
import Image
def demo():
	#packer = Packer(100, 50)  # or:  new GrowingPacker();
	packer = GrowingPacker(256, 512)  # or:  new GrowingPacker();
	nodes=[]
	for i in range(30):
		node=Node(random.randint(10,100),random.randint(10,100))
		nodes.append(node)
	#nodes = [
	#   Node(100,100),Node(10,100),Node(80,80),Node(80,80) ]
	#mysort(nodes)#.sort()#function(a,b) { return (b.h < a.h); }); // sort inputs for best results
	#nodes.sort(key=lambda var:var.h*var.w, reverse=True)
	nodes.sort(key=lambda var:var.h, reverse=True)
	packer.fit(nodes);
	for n in range(len(nodes)):
	    block = nodes[n];
	    if (block.fit!=None):
	      print(block.fit.x, block.fit.y, block.w, block.h,block.fit.used)
	    else:
	      print(block.x, block.y, block.w, block.h,block.used)
	print packer.root.w,packer.root.h
	return(packer,nodes)
if __name__=="__main__":
	demo()
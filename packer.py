class Node:
    def __init__(self, w, h, x=0, y=0):
        self.used=False
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.fit=None
class Packer:# = function(w, h) {
  def __init__(self,w,h):
    self.init(w, h);
  def init(self,w, h) :
    self.root = Node( w, h )
  def fit(self,blocks):
    #n, node, block;
    for n in range(len(blocks)):#(n = 0; n < blocks.length; n++) {
      block = blocks[n];
      node = self.findNode(self.root, block.w, block.h)
      if node!=None:
        block.fit = self.splitNode(node, block.w, block.h);
  def findNode(self,root, w, h) :
    if (root.used):
      return self.findNode(root.right, w, h) or self.findNode(root.down, w, h);
    elif ((w <= root.w) and (h <= root.h)):
      return root;
    else:
      return None;
  def splitNode(self,node, w, h) :
    node.used = True;
    node.down  = Node( node.w,     node.h - h,node.x,      node.y + h)
    node.right = Node( node.w - w,  h      , node.x + w,  node.y)
    return node;
class GrowingPacker(Packer):
  def fit(self,blocks):
    #var n, node, block, 
    lenn = len(blocks)
    if lenn > 0:
      w=blocks[0].w
      h=blocks[0].h
    else:
      w=0
      h=0
    self.root = Node(w,h)#x: 0, y: 0, w: w, h: h };
    for  n in range(lenn):
      block = blocks[n]
      node = self.findNode(self.root, block.w, block.h)
      if (node !=None):
        block.fit = self.splitNode(node, block.w, block.h);
      else:
        block.fit = self.growNode(block.w, block.h);

  # def findNode(self,root, w, h) :
  #   if (root.used):
  #     return self.findNode(root.right, w, h) or self.findNode(root.down, w, h);
  #   elif ((w <= root.w)  and (h <= root.h)):
  #     return root;
  #   else:
  #     return None;

  # def splitNode(self,node, w, h) :
  #   node.used = True;
  #   node.down  = { x: node.x,     y: node.y + h, w: node.w,     h: node.h - h };
  #   node.right = { x: node.x + w, y: node.y,     w: node.w - w, h: h          };
  #   return node;
  # },

  def growNode(self,w, h):
    canGrowDown  = (w <= self.root.w)
    canGrowRight = (h <= self.root.h)

    shouldGrowRight = canGrowRight  and  (self.root.h >= (self.root.w + w)); # attempt to keep square-ish by growing right when height is much greater than width
    shouldGrowDown  = canGrowDown  and  (self.root.w >= (self.root.h + h)); # attempt to keep square-ish by growing down  when width  is much greater than height

    if (shouldGrowRight):
      return self.growRight(w, h);
    elif (shouldGrowDown):
      return self.growDown(w, h);
    elif (canGrowRight):
     return self.growRight(w, h);
    elif (canGrowDown):
      return self.growDown(w, h);
    else:
      return None # need to ensure sensible root starting size to avoid self happening
  def growRight(self,w, h):
    newroot =Node(self.root.w + w,self.root.h) 
    newroot.down=self.root
    newroot.right=Node(w,self.root.h,self.root.w,  0)
    newroot.used=True
    self.root=newroot
    node = self.findNode(self.root, w, h)
    if (node !=None):
      return self.splitNode(node, w, h);
    else:
      return None;
  def growDown(self,w, h):
    newroot = Node(self.root.w,self.root.h + h)
    newroot.down=Node( self.root.w, h ,0,self.root.h)
    newroot.right=self.root
    newroot.used=True
    self.root=newroot
    node = self.findNode(self.root, w, h)
    if (node !=None):
      return self.splitNode(node, w, h);
    else:
      return None

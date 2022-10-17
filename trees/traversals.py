
class Node: 
  def __init__(self, data): 
    self.left = None    
    self.right = None   
    self.data = data    

  def insert(self, data): 
    
    if self.data: 
      if data < self.data: 
        if self.left is None:
          self.left = Node(data) 
        else:
          self.left.insert(data) 
      elif data > self.data:  
        if self.right is None:    
          self.right = Node(data)
        else : 
          self.right.insert(data)
    else:  
      self.data = data 


  def PrintTree(self): # in-order printing though
    if self.left: 
      self.left.PrintTree() 
    print(self.data) 
    if self.right: 
      self.right.PrintTree() 
    


a = Node(6)
a.insert(2)
a.insert(3)
a.insert(5)
a.insert(3)
a.insert(8)


# in-order : left->root->right
def inOrder( root: Node ): 

    out = []

    if root: 
        out = inOrder(root.left) #left
        out.append(root.data) #root
        out = out + inOrder(root.right)  #right
    
    return out

print('In-Order: ', inOrder(a))

def postOrder(root: Node):
    out = []

    if root:
        out = postOrder(root.left) #left
        out = out + postOrder(root.right) #right
        out.append(root.data) #root
    
    return out

print('Post order is: ', postOrder(a))

# post-order left->right->root

# pre-order root->left-right
def preOrder(root: Node): 

    out = []

    if root: 
        out.append(root.data)
        out = out + preOrder(root.left)
        out = out + preOrder(root.right)
    
    return out 


print('Pre Order', preOrder(a))
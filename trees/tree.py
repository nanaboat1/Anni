# implementation of trees
# class TreeNode {
#   int data;
#   TreeNode left;
#   TreeNode right;
# }


class Node:
    def __init__(self, data) -> None:
        
        #right child
        self.right = None
        #left child
        self.left = None
        #data
        self.data = data

    ## in-order => tree prints from left to right
    def __repr__(self): 
        return f'{self.data}'

    #inserting things into a tree
    def insert(self, data):
        if self.data:
            if data < self.data:
                #left
                if self.left == None:
                    self.data = Node(data)
                else: self.left.insert(data)
            elif data > self.data:
                #right
                if self.right == None:
                    self.data = Node(data)
                else: self.right.insert(data)

        else: 
            self.data = data  
    
    ## printing items in a tree
    def printTree(self): 
        if self.left: 
            self.left.printTree()
        print(self.data)
        if self.right: 
            self.right.printTree()
    ## 


# implementing the tree. 
root = Node(8)

        


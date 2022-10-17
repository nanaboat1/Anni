#
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
    def insert(self, node):

        if self.data:
            if node < self.data:
                #left
                if self.left == None:
                    self.left = Node(node)
                else: self.left.insert(node)
            elif node > self.data:
                #right
                if self.right == None:
                    self.right = Node(node)
                else: self.right.insert(node)

        else: 
            self.data = node 
        
    
    ## printing items in a tree
    def printTree(self): 
        if self.left: 
            self.left.printTree()
        print(self.data)
        if self.right: 
            self.right.printTree()
    ## 


class Tree: 

    def __init__(self, nodes : list= []): 
        self.root : Node = None 

        if nodes and len(nodes) == 0: 
            return 
        if nodes is not None: 
            node : Node = Node(data=nodes.pop(0))
            self.root = node 
        

        # add subsequent elements to the root node.
        for elem in nodes: 
            self.root.insert(elem)


# implementing the tree. 

a = Tree([3,4,5,6,2,1])


# implementation of trees

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
        return f'{self.data}-->'
        


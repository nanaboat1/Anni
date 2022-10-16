# anni and nana

# impl node class
class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.next = None 

def __repr__(self):
    return f'{self.data}->{self.next}'

# impl linked-list class
class LinkedList: 

    def __init__(self, nodes=None) -> None:
        self.head = None 
        if nodes and len(nodes) == 0: 
            return 
        if nodes is not None: 
            node : Node = Node(data=nodes.pop(0))
            self.head = node 
        

            # add subsequent elements to the node. 
            for elem in nodes: 
                node.next = Node(data=elem)
                node = node.next # itr over linkedlist
    
    def __repr__(self) -> str:
        node = self.head
        nodes = []

        while node is not None: 
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


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
###

#.1 merging sorted linkedlists. 
# UMPIRE
# u -> Edge Cases:   a = ! or b = ! or a and b =null
# m -> itr over the linkedlist and find the smallest that exists and (create new linkedlist or something else)
# p -> use pseudocode from whiteboard.

def mSort( a : LinkedList, b : LinkedList) -> LinkedList: 

    # edge-case
    # if not a and not b: return a
    if not a : return b
    if not b : return a 

    # dummy for both a and b
    curA = a.head 
    curB = b.head 
    nr = LinkedList(nodes = [-1])
    dum = out = nr.head

    while curA and curB: 

        if curA.data < curB.data:
            out.next = curA 
            curA = curA.next # itr next node
            
        else: 
            out.next = curB 
            curB = curB.next # point to next node
        
        out = out.next

    # if one linkedlist is smaller than the other, append whatever is left on the list to out
    if not curA : out.next = curB 
    if not curB : out.next = curA

    return dum

m , n = LinkedList([1,2,4,5,6,7,8,9]), LinkedList([1,3,4])

# Remove Nth Node from End of List
# Given a linked list, remove the n-th node from the end of list and return its head.

def rmvNode( a: LinkedList, idx : int) : 
    #O(N)
    arr = [] # creating new array to store linkedlist data
    b = h = a_head = a.head
    
    # while h:
    #     arr.append(h.data)
    #     h = h.next

    # #remove nth item from end of the node
    # arr.remove(arr[len(arr) - idx])

    # a_edited = LinkedList(arr)
    # a_head = a_edited.head

    #O(1)
    count = 0
    #finding the length of the linkedlist
    while h:
        h = h.next
        count += 1
    #we now have count = len(linkedlist)
    # print(count)
    removee = count - idx #index where we need to remove item
    print(removee)
    countt = 0
    while b: 
        if countt == removee - 1:
            b.next = b.next.next
        countt += 1
        b = b.next
    return a_head


#rmvNode(m, 3)


x = rmvNode(m,3)
# print(x)
while x:
    print(x.data, end=" ")
    x = x.next
    




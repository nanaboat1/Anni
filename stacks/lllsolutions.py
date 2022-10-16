###
#.1 merging sorted linkedlists. 
# UMPIRE
# u -> Edge Cases:   a = ! or b = ! or a and b =null
# m -> itr over the linkedlist and find the smallest that exists and (create new linkedlist or something else)
# p -> use pseudocode from whiteboard.

"""
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


Print out the first intersection of between two-linked lists.
If the two linked lists have no intersection at all, return null.

Example : intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], Output = 8
"""

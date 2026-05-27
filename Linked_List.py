# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# def traverseList(head):
#     while head is not None:
#         print(head.data, end="")
#         if head.next is not None:   
#             print(" -> ", end="")
#         head = head.next
#     print()

# def insertAtFront(head,x):
#     NewNode = Node(x)
#     NewNode.next = head
#     return NewNode

# def insertAtEnd(head,x):
#     NewNode = Node(x)
#     if head is None:
#         return NewNode
#     last = head
#     while last.next is not None:
#         last=last.next
#     last.next=NewNode
#     return head
# def inserAtMiddle(head,pos,val):
#     if pos <1:
#         return head
#     if pos == 1:
#         newNode = Node(val)
#         newNode.next = head
#         return newNode

#     curr = head
#     for i in range (1,pos-1):
#          if curr is None:
#             return head
#          curr = curr.next

#     if curr is None:
#         return head
#     NewNode = Node(val)
#     NewNode.next = curr.next
#     curr.next = NewNode
#     return head
# def deleteAtBeginning(head):
#     if head is None:
#         return head
#     temp = head
#     head = head.next
#     temp = None
#     return head
# def deleteAtEnd(head):
#     if head is None:
#         return None
#     if head.next is None:
#         return None
#     secondlast = head
#     while secondlast.next.next is not None:
#         secondlast = secondlast.next
#     secondlast.next = None
#     return head
# def deleteAtMiddle(head,pos):
#     temp = head
#     if pos == 1:
#         head = temp.next
#         return head
#     prev = None
#     for i in range(1, pos):
#         prev = temp
#         temp = temp.next	

#     prev.next = temp.next
#     return head
# def searching(head,key):
#     current = head
#     while current is not None:
#         if current.data == key:
#          return True
#         current = current.next
#     return False
# def reverseList(head):
#     current = head
#     prev = None
#     while current is not None:
#         Nextnode = current.next
#         current.next = prev
#         prev=current
#         current = Nextnode
#     return prev



# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# # x=50
# # head = insertAtFront(head,x)
# # head = insertAtEnd(head,x)
# # val, pos = 25, 3
# # head = inserAtMiddle(head, pos, val)
# # head = deleteAtBeginning(head) 
# # head = deleteAtEnd(head) 
# # head = deleteAtMiddle(head,3)
# # key = 5
# # if searching(head, key):
# #         print("true")
# # else:
# #     print("False")
# # head = reverseList(head)

# traverseList(head)







                     #Doubly linked list






class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
def traverseList(head):
    while head is not None:
        print(head.data, end="")
        if head.next is not None:   
            print(" <-> ", end="")
        head = head.next
    print()
def inser_At_Front(head,x):
    Newnode = Node(x)
    Newnode.next = head
    if head is not None:
        head.prev = Newnode
    return Newnode
def inser_At_End(head,x):
    Newnode = Node(x)
    if head is None:
        head = Newnode
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = Newnode
        Newnode.prev = curr
        return head
def insertAtPos(head, pos, new_data):
    new_node = Node(new_data)
    if pos == 1:
        new_node.next = head
        if head is not None:
            head.prev = new_node
        head = new_node
        return head
    curr = head
    for i in range(1, pos - 1):
        if curr is None:
            break
        curr = curr.next
    if curr is None:
        return head
    new_node.prev = curr
    new_node.next = curr.next
    curr.next = new_node
    if new_node.next is not None:
        new_node.next.prev = new_node
    return head
def Delete_At_Front(head):
    if head is None:
        return None
    temp = head
    head = head.next
    if head is not None:
        head.prev = None
    return head
def del_last(head):
    if head is None:
        return None
    if head.next is None:
        return None
    curr = head
    while curr.next is not None:
        curr = curr.next
    if curr.prev is not None:
        curr.prev.next = None
    return head
def delPos(head, x):
    if head is None:
        return head  
    curr = head
    for i in range(1, x):
        if curr is None:
            return head  
        curr = curr.next

    if curr is None:
        return head  
    if curr.prev is not None:
        curr.prev.next = curr.next
    if curr.next is not None:
        curr.next.prev = curr.prev
    if head == curr:
        head = curr.next
    del curr
    return head








head = Node(10)
head.next = Node(20)
head.next.prev = head
head.next.next = Node(30)
head.next.next.prev = head.next
head.next.next.next = Node(40)
head.next.next.next.prev = head.next.next


# head = inser_At_Front(head,5)
# head = inser_At_End(head,5)
# data = 3
# pos = 3
# head = insertAtPos(head, pos, data)
# head = Delete_At_Front(head)
# head = delPos(head, 2)
traverseList(head)


#           single and double circular linked list

#                                                 Basics of treeeeeeeeeee
# import sys
# class Node:
#     def __init__(self,x):
#         self.data = x
#         self.children = []

# def addChild(parent,child):
#     parent.children.append(child)
# def printParents (node,parent):
#     if parent is None:
#         print(str(node.data)+"-> NULL")
#     else:
#         print(str(node.data) + " -> " + str(parent.data))
#     for child in node.children:
#         printParents(child, node)
# def printChild(node):
#     children_str = " ".join(str(child.data) for child in node.children)
#     print(str(node.data) + " -> " + children_str)
#     for child in node.children:
#         printChild(child)
# def printLeafNodes(node):
#     if not node.children:
#         sys.stdout.write(str(node.data) + " ")
#         return
#     for child in node.children:
#         printLeafNodes(child)


# root = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(6)
# n7 = Node(7)

# addChild(root, n2)
# addChild(root, n3)
# addChild(n2, n4)
# addChild(n2, n5)
# addChild(n3, n6)
# addChild(n3, n7)

# print("Parents of each node:")
# printParents(root, None)

# print("Children of each node:")
# printChild(root)

# print("Leaf nodes: ")
# printLeafNodes(root)
# print("\n")



#                                        binary Treeeeeeeeeeeeeeeeeeeeeeeeeeeee


#                                        Binary treeeeeee Traversal


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
    
# def Inorder (node,res):
#     if node is None:
#         return
#     Inorder(node.left,res)
#     res.append(node.data)
#     Inorder(node.right,res)

# def preOrder(node,res):
#     if node is None:
#         return
#     res.append(node.data)
#     preOrder(node.left,res)
#     preOrder(node.right,res)
# def postOrder(node,res):
#     if node is None:
#         return
#     postOrder(node.left,res)
#     postOrder(node.right,res)
#     res.append(node.data)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.right = Node(6)
# In=[]
# Pre=[]
# Post=[]
# Inorder(root,In)
# preOrder(root,Pre)
# postOrder(root,Post)
# for node in In:
#     print(node,end=" ")
# print()
# for node in Pre:
#     print(node,end=" ")
# print()
# for node in Post:
#     print(node,end=" ")
# print()










#                                        Binary treeeeeee Traversal level order (Breadth first search)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None


# def levelOrder(root):
#     if root is None:
#         return []
    
#     q=[]
#     res=[]

#     q.append(root)
#     level = 0
    
#     while q:
#         queue_length = len(q)
#         res.append([])
#         for _ in range (queue_length):
#             node = q.pop(0)
#             res[level].append(node.data)

#             if node.left is not None:
#                 q.append(node.left)
#             if node.right is not None:
#                 q.append(node.right)
#         level+=1
#     return res


# root = Node(5)
# root.left = Node(12)
# root.right = Node(13)
# root.left.left = Node(7)
# root.left.right = Node(14)
# root.right.right = Node(2)
# root.left.left.left = Node(17)
# root.left.left.right = Node(23)
# root.left.right.left = Node(27)
# root.left.right.right = Node(3)
# root.right.right.left = Node(8)
# root.right.right.right = Node(11)

# res = levelOrder(root)
# for level in res:
#     for val in level:
#         print(val, end=' ')
#     print()
    




#                                            Height of binary treeeeeeeee

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None
# def height(root):
#     if root is None:
#          return -2
#     lHeight = height(root.left)
#     rHeight = height(root.right)

#     return max(lHeight, rHeight) + 1


# root = Node(12)
# root.left = Node(8)
# root.right = Node(18)
# root.left.left = Node(5)
# root.left.right = Node(11)

# print(height(root))








#                                              Searching in Binary tree

# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.left = None
#         self.right = None
# def ifNodeExists(root, key):
#     if root is None:
#         return False
#     if root.data == key:
#         return True
#     res1 = ifNodeExists(root.left, key)
#     if res1:
#         return True
#     res2 = ifNodeExists(root.right, key)

#     return res2



# root = Node(0)
# root.left = Node(1)
# root.left.left = Node(3)
# root.left.left.left = Node(7)
# root.left.right = Node(4)
# root.left.right.left = Node(8)
# root.left.right.right = Node(9)
# root.right = Node(2)
# root.right.left = Node(5)
# root.right.right = Node(6)
# key = 4
# if ifNodeExists(root, key):
#     print("True")
# else:
#     print("False")






#                                            Insersion Binary treeeeeee

# from collections import deque
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# def InserData(root,data):
#     if root is None:
#         root = Node(data)
#         return root
#     q=deque()
#     q.append(root)
#     while q:
#         curr=q.popleft()
#         if curr.left is not None:
#             q.append(curr.left)
#         else:
#             curr.left = Node(data)
#             return root
#         if curr.right is not None:
#             q.append(curr.right)
#         else:
#             curr.right = Node(data)
#             return root
# def inorder(curr):
#     if curr is None:
#         return
#     inorder(curr.left)
#     print(curr.data, end=' ')
#     inorder(curr.right)
    


# root = Node(10)
# root.left = Node(11)
# root.right = Node(9)
# root.left.left = Node(7)
# root.right.left = Node(15)
# root.right.right = Node(8)
# key = 12
# root = InserData(root, key)
# inorder(root)



#                                        Deletion in binary treeeeeeeeeeee



# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.left = None
#         self.right = None

# def deletion(root, key):

#     if root is None:
#         return None

#     if root.left is None and root.right is None:
#         if root.data == key:
#             return None
#         return root

#     queue = [root]
#     curr = None
#     keyNode = None

#     while queue:

#         curr = queue.pop(0)      

#         if curr.data == key:     
#             keyNode = curr       

#         if curr.left:
#             queue.append(curr.left)

#         if curr.right:
#             queue.append(curr.right)

#     if keyNode is not None:

#         x = curr.data

#         keyNode.data = x

#         delete_deepest(root, curr)

#     return root


# def delete_deepest(root, dNode):
#     queue = [root]

#     while queue:
#         curr = queue.pop(0)
#         if curr == dNode:
#             curr = None
#             del dNode
#             return
#         if curr.right:
#             if curr.right == dNode:
#                 curr.right = None
#                 del dNode
#                 return
#             queue.append(curr.right)

#         if curr.left:
#             if curr.left == dNode:
#                 curr.left = None
#                 del dNode
#                 return
#             queue.append(curr.left)


# def inorder(curr):
#     if curr is None:
#         return
#     inorder(curr.left)
#     print(curr.data, end=" ")
#     inorder(curr.right)

# root = Node(10)
# root.left = Node(11)
# root.right = Node(9)
# root.left.left = Node(7)
# root.left.right = Node(12)
# root.right.left = Node(15)
# root.right.right = Node(8)

# key = 11
# root = deletion(root, key) 

# inorder(root)


#                                      Binary search treeeeeeeeeeee





# class Node:
#     def __init__(self, item):
#         self.data = item
#         self.left = None
#         self.right = None


# def search(root,key):
#     if root is None:
#         return False
#     if root.data == key:
#         return True
#     if key > root.data:
#         return search(root.right,key)
#     return search(root.left,key)




# root = Node(6)
# root.left = Node(2)
# root.right = Node(8)
# root.right.left = Node(7)
# root.right.right = Node(9)

# key = 7
# print(search(root, key))




#                                 insertion in binary search treeeeeeeeeee




# class Node:
#     def __init__(self, item):
#         self.data = item
#         self.left = None
#         self.right = None

# def insert(root,key):
#     if root is None:
#         return Node(key)
#     if key < root.data :
#         root.left = insert(root.left, key)
#     else: 
#         root.right = insert(root.right, key)
#     return root

# def inorder(curr):
#     if curr is None:
#         return
#     inorder(curr.left)
#     print(curr.data, end=" ")
#     inorder(curr.right)

# root = Node(6)
# root.left = Node(2)
# root.right = Node(8)
# root.right.left = Node(7)
# root.right.right = Node(9)
# root = insert(root, 45) 
# root = insert(root, 10) 
# inorder(root)



#                            Deletion in binary search treeeeeeeeeeeee


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def getsuccessor (curr):
#     curr = curr.right
#     while curr.right is not None and curr.left is not None:
#         curr = curr.left
#     return curr

# def Deletion(root,key):
#     if root is None:
#         return None
#     if root.data > key:
#         root.left = Deletion(root.left,key)
#     elif root.data < key:
#         root.right = Deletion(root.right, key)
#     else:
#         if root.left is None:
#             return root.right
#         if root.right is None:
#             return root.left
#         succ = getsuccessor(root)
#         root.data = succ.data
#         root.right = Deletion(root.right, succ.data)
#     return root


# def inorder(curr):
#     if curr is None:
#         return
#     inorder(curr.left)
#     print(curr.data, end=" ")
#     inorder(curr.right)

# root = Node(50)
# root.left = Node(40)
# root.right = Node(60)
# root.right.left = Node(55)
# root.right.right = Node(65)
# root.left.left = Node(20)
# root.left.right = Node(45)
# # key = 60
# # root = Deletion(root,key)
# inorder(root)


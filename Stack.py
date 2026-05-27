#  Implementinf Stack

MAXSIZE=8
stack=[0]*MAXSIZE
top=-1
def isFull():
    if top==MAXSIZE-1:
        return 1
    else:
        return 0
    
def isEmpty():
    if top == -1:
        return 1
    else:
        return 0
    
def peek():
    return stack[top]
    
def traverse(stack):
    print("Stack Content :")
    for i in range(top + 1):
        print(stack[i])
    
def push(data):
    global top
    if isFull() != 1:
        top=top + 1
        stack[top]=data
    else:
        print("Stack is full")
        return data
    

def pop():
    global top
    if not isEmpty() :
        poped = stack[top]
        top = top - 1
        return poped

    else:
        print("Stack is empty")
        return None


push(0)
push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)

traverse(stack)


print("popped",pop())
print("popped",pop())


traverse(stack)


#                   implementing stack using list




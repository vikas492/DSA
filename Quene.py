# max = 5
# Queue = [0] * max
# front=-1
# rear=-1

# def isFull():
    
#     return rear == max-1

# def isEmpty():
    
#     return front == -1 or front > rear
# def enqueue(data):
#     global rear,front
#     if isFull():
#         print("the quene is full no place for insertion")
#         return
#     if front == -1:
#         front = 0
#     rear += 1
#     Queue[rear] = data
#     print(f"Enqueued: {data}")

# def dequeue():
#     global front
#     if isEmpty():
#         print("Queue is empty, nothing to dequeue.")
#         return None
#     removed = Queue[front]
#     front += 1
    
#     return removed
       
# enqueue(23)
# enqueue(34)    
# enqueue(34) 
# enqueue(34) 
# enqueue(34) 
# print(f"dequeue : {dequeue()}")
# print(f"dequeue : {dequeue()}")
# enqueue(34)  # this is the condition where the one dimensional queue gets full even though their is space and we need to use the circular queue instead






#                    implementing circular queue



max = 5
Queue = [0] * max
front=-1
rear=-1
itemsCount = 0
def isFull():
    
    return itemsCount == max      #changed for circular queue

def isEmpty():
    
    return itemsCount == 0        #changed for circular queue
def enqueue(data):
    global rear,front,itemsCount
    if isFull():
        print("the quene is full no place for insertion")
        return
    if front == -1:
        front = 0
    rear = (rear+1)%max          #changed for circular queue
    Queue[rear] = data
    itemsCount+=1
    print(f"Enqueued: {data}")

def dequeue():
    global front,itemsCount
    if isEmpty():
        print("Queue is empty, nothing to dequeue.")
        return None
    removed = Queue[front]
    itemsCount-=1
    front = (front+1)%max       #changed for circular queue
    
    return removed


enqueue(1)
enqueue(2)    
enqueue(3) 
enqueue(4) 
enqueue(5) 
print(f"dequeue : {dequeue()}")
print(f"dequeue : {dequeue()}")
enqueue(6)  




#                   implementing double ended queue ( deleting and inserting from the same end of the queue)

















#                     implementing queue using list
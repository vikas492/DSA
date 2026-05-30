# Learning Arrays Properly 
# First solving basic problems to have hands on arrays. Later increasing the level


#*******************************************************Basics for Array*************************************************************


#                                                                              Alternate elements of an array

# arr=[10,20,30,40,50,60,70,80,90,100]
# result=[]
# for i in range (0,len(arr),2):
#     result.append(arr[i])
# print(" ".join(map(str,result)))

#                                                                              Move all Zeros to End of Array

# arr=[10,20,0,40,0,60,0,80,90,10]
# length = len(arr)
# result=[0]*length
# j=0
# for i in range(length):
#     if arr[i] != 0:
#         result[j] = arr[i]
#         j+=1
# while j < length:
#     result[j] = 0
#     j+=1
# for i in range (length):
#     arr[i]=result[i]

# print(" ".join(map(str,arr))) # use pointers for this sum

#                                                                            Move all Zeros to End of Array using pointers


# arr=[10,20,0,40,0,60,0,80,90,10]
# count = 0
# for i in range (len(arr)):
#     if  arr[i] != 0:
#         arr[i],arr[count] = arr[count] ,arr[i]
#         count+=1
# for i in range(len(arr)):
#    print(arr[i],end=" ")


#                                                                            Move all Zeros to End of Array using pointers


# arr=[10,20,0,40,0,60,0,80,90,10]  
# count = 0
# for i in range (len(arr)):
#     if arr[i] != 0:
#         arr[count] = arr[i]
#         count+=1
# while count<len(arr):
#     arr[count] = 0
#     count+=1
# for i in range (len(arr)):
#     print(arr[i],end=" ")


#                                                                             Array Reverse

#                                                                             Array reverse using normal meathod


# arr = [10,20,30,40,50,60,70,80,90,100]
# result = []
# # for i in range (len(arr)-1,-1,-1):
# #     print(arr[i],end=" ")
# # print()
# for i in range (len(arr)-1,-1,-1):
#    result.append(arr[i])
# # print(" ".join(map(str,result)))

# for i in range (len(arr)):
#    arr[i]=result[i]
# # print(" ".join(map(str,arr)))

# for i in range(len(arr)):
#    print(arr[i],end=" ")


#                                                                            Array reverse using two pointer


# arr = [10,20,30,40,50,60,70,80,90,100]
# left = 0
# right = len(arr)-1
# while left < right :
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# for i in range (len(arr)):
#     print(arr[i],end=" ")

#                                                                           Array reverse using single pointer


# arr = [10,20,30,40,50,60,70,80,90,100]
# n=len(arr)
# for i in range (n//2):
#     temp = arr[i]
#     arr[i]=arr[n-i-1]
#     arr[n-i-1]=temp
# for i in range (len(arr)):
#     print(arr[i],end=" ")


 
#                                                                           Remove dublicates from an Arrays


# arr=[1,2,2,3,3,3,4,4,4]
# seen = set()
# idx=0
# for i in range (len(arr)):
#     if arr[i] not in seen:
#         seen.add(arr[i])
#         arr[idx] = arr[i]
#         idx += 1
# print(arr[:idx])


#                                                                           Removing dublicate by simple meathod


# arr=[1,2,2,3,3,3,4,4,4]
# res = []
# for i in range (len(arr)):
#     if arr[i] not in res:
#         res.append(arr[i])
# print(res)



#                                                                           leader in an array


# arr=[10,22,12,3,0,6]
# leaders=[]

# for i in range (len(arr)):
#     isLeader = True
#     for j in range (i+1,len(arr)):
#         if arr[j]>arr[i]:
#             isLeader = False
#             break
#     if isLeader:
#             leaders.append(arr[i])

# print(leaders)


#                                                                          optimal leader in an array 


# arr=[10,22,12,3,0,6]
# n=len(arr)

# maxRight=arr[-1]
# result=[]
# result.append(maxRight)
# for i in range (n-2,-1,-1):
#     if arr[i]>maxRight:
#         maxRight=arr[i]
#         result.append(arr[i])

# result.reverse()
# print(result)

#                                                                         Generating all subarrays
        


# arr=[1,2,3,4,5]
# n=len(arr)
# for i in range (n):
#     for j in range (i,n):
#         for k in range (i,j+1):
#             print(arr[k],end=" ")
#         print()



#                                                                         Generating all subarrays using slicing

# arr=[1,2,3,4,5]
# n=len(arr)
# for i in range (n):
#     for j in range (i,n):
#         print(arr[i:j+1])


#                                                                         Array rotation by d (one to one rotation)


# arr=[1,2,3,4,5]
# n=len(arr)
# d=2
# for _ in range (d):
#     last = arr[n-1]
#     for i in range (n-1,0,-1):
#         arr[i]=arr[i-1]
#     arr[0]=last
# print(arr)


#                                                                        Array rotation using slice


# arr=[1,2,3,4,5]
# d=3
# arr.reverse()
# print(arr)
# arr[:d]=reversed(arr[:d])
# print(arr[:d])
# arr[d:]=reversed(arr[d:])
# print(arr[d:])
# for i in range(len(arr)):
#         print(arr[i], end=" ")





#************************************Moving deep in arrays by solving sums (Sums will include various techniques and algorithms)*************************
#******************************************************************Every Thing will be Mensioned**************************************************************
#****************************************************Solving some sums from the youtube channel Move U forward*****************************************************

# arr=[2,4,6,23,16,80,64,3]
# n=len(arr)
# for i in range(n):
#     swapped=False
#     j=0
#     for j in range(0,n-i-1):                                                       ## Largest Element (Brute Force)
#         if arr[j]>arr[j+1]:
#            arr[j],arr[j+1]=arr[j+1],arr[j]
#            swapped = True
#     if swapped == False:
#             break
# print(arr)
# largest = arr[n-1]
# print(largest)





# arr=[2,4,6,90,16,80,64,3]
# n=len(arr)
# Largest = arr[0]
# for i in range (1,n):                                                              ## Optimal approch for Largest in an array
#     if arr[i]>Largest:
#         Largest = arr[i]
# print(Largest)







# arr=[2,4,6,23,16,80,64,3]
# n=len(arr)
# for i in range(n):
#     swapped=False
#     j=0
#     for j in range(0,n-i-1):                                                       ## Second Largest Element (Brute Force)
#         if arr[j]>arr[j+1]:                                                        ## This will fail if the array becomes [....,80,80]
#            arr[j],arr[j+1]=arr[j+1],arr[j]
#            swapped = True
#     if swapped == False:
#             break
# print(arr)
# largest = arr[n-2]
# print(largest)




# arr=[2,4,80,23,16,80,64,80]
# n=len(arr)
# for i in range(n):
#     swapped=False
#     j=0
#     for j in range(0,n-i-1):                                                       ## Second Largest Element (Brute Force)
#         if arr[j]>arr[j+1]:                                                        ## This will work
#            arr[j],arr[j+1]=arr[j+1],arr[j]
#            swapped = True
#     if swapped == False:
#             break
# print(arr)
# largest = arr[n-1]
# print(largest)
# secondLargest = 0
# for i in range(n-2,-1,-1):
#      if arr[i]!=largest:
#           secondLargest = arr[i]
#           break
# print(secondLargest)
          


# arr=[2,7,3,9,5,19,14,12]
# n=len(arr)
# Largest = 0
# secondLargest = -1
# for i in range (n):
#     if arr[i]>Largest:
#         secondLargest = Largest
#         Largest = arr[i]
        
#     elif arr[i]>secondLargest and arr[i]<Largest:
#         secondLargest = arr[i]

# print(f"Largest Element is : {Largest} and Second Largest element is : {secondLargest}")



# a=[3,2,4,1,5]
# a=[1,2,3,4,5]
# a=[22,33,44,56,67,78]
# n=len(a)
# sorted=True
# for i in range (1,n):
#     if a[i]>a[i-1]:                            #look for the sign < and >
#         sorted=False
#         break
# print(sorted)




# arr=[1,1,2,2,2,3,3,3,3]
# res=set()
# for i in range(0,len(arr)):
#     res.add(arr[i])
# print(res)
# print(list(res))




# arr=[1,1,2,2,2,3,3,3,3]
# def removeDublicate(arr):
#     i=0
#     for j in range (len(arr)):
#         if arr[j] != arr[i]:
#             arr[i+1]=arr[j]
#             i+=1
#     return i+1
# print(removeDublicate(arr))





# arr=[1,2,3,4,5]
# temp = arr[0]
# for i in range (1,len(arr)):
#     arr[i-1] = arr[i]
    
# arr[len(arr)-1]=temp
# print(arr)


arr=[1,2,3,4,5,6]
n=len(arr)
temp=[]
d=3
d=d%n
for i in range (d):
    temp.append(arr[i])
print(temp)
for i in range (d,len(arr)):
    arr[i-d]=arr[i]
print(arr)
j=0
for j in range (len(temp)):
    arr[n-d+j]=temp[j]
print(arr)






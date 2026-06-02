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
#     if arr[i]>Largest:                                                               #optimal of second Largest Element
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
#     if a[i]>a[i-1]:                                                                 #look for the sign < and >
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
#     arr[i-1] = arr[i]                                                         #shift by one position
    
# arr[len(arr)-1]=temp
# print(arr)







# arr=[1,2,3,4,5,6]
# n=len(arr)
# temp=[]
# d=3
# d=d%n
# for i in range (d):
#     temp.append(arr[i])
# print(temp)
# for i in range (d,len(arr)):                                                # the space complexity is o(d) to reduce it will do reverse meathod
##                                                                              # the reverse method is solved above
#     arr[i-d]=arr[i]
# print(arr)
# j=0
# for j in range (len(temp)):
#     arr[n-d+j]=temp[j]
# print(arr)



# a1=[1,2,2,3,3,4,4,4,4,5]
# a2=[1,2,3,4,4,5,6,7]

# res=set()
# for i in range (len(a1)):                                                  # Union brute force
#     res.add(a1[i])
# print(res)
# for i in range (len(a2)):
#     res.add(a2[i])
# print(res)
# union=(list(res))
# print(union)




# a1=[1,2,2,3,3,4,4,4,4,5]
# a2=[1,2,3,4,4,5,6,7]
# union = []
# i=0
# j=0
# while i<len(a1) and j<len(a2):
#     if a1[i]<=a2[j]:
#         if len(union)==0 or union[-1]!=a1[i]:
#             union.append(a1[i])
#         i+=1
#     else:
#         if len(union)==0 or union[-1]!=a2[j]:                                   #optimal solution for union
#                  union.append(a2[j])
#         j+=1
# while i<len(a1):
#     if union[-1]!=a1[i]:
#         union.append(a1[i])
#     i+=1
# while j<len(a2):
#     if union[-1]!=a2[j]:
#         union.append(a2[j])
#     j+=1
# print(union)






# a1=[1,2,2,3,3,4,4,4,4,5]
# a2=[1,2,3,4,4,5,6,7]
# intersection = []
# i=0
# j=0
# while i<len(a1) and j<len(a2):
#     if a1[i]<a2[j]:
#         i+=1                                                                       # Optimized insertion
#     elif a2[j]<a1[i]:
#             j+=1
#     else:
#         if len(intersection)==0 or intersection[-1]!=a1[i]:
#             intersection.append(a1[i])
#         i+=1
#         j+=1
# print(intersection)
        
         
        
    

# arr=[1,2,3,4,6]
# n=len(arr)+1
# for i in range (1,n+1):
#     flag=0
#     for j in range (len(arr)):                                                # Brute force for missing one Element
#         if i == arr[j]:
#             flag = 1
#             break
#     if flag==0:
#         print(i)
#         break



# arr=[1,2,3,4,6]
# n=len(arr)+1
# hashArr = [0]*(n+1)
# for i in range (len(arr)):                                                   # Better approch using hashing
#     hashArr[arr[i]] = 1
# for i in range (1,n+1):
#     if hashArr[i]==0:
#         print(i)
#         break




# arr=[1,2,3,4,6]
# n=len(arr)+1
# Total=0
# sum=n*(n+1)/2
# for i in range (len(arr)):                                                    # Optimum approch one using formula 
#     Total+=arr[i]
# missing = sum-Total
# print(int(missing))




# arr=[1,2,3,4,5,6,8]
# n=len(arr)+1
# xor1=0
# xor2=0
# for i in range (1,n+1):                                                         # Optimum approch two using XOR O(2N)
#     xor1^=i                                                                     # it can be solves in one loop look for the more optimum approch
# for num in arr:
#     xor2^=num
# missing=xor1^xor2
# print(missing)




# arr = [1,2,3,4,6,7,8]
# n = len(arr)+1
# xor1 = 0
# xor2 = 0
# for i in range(n - 1):
#     xor2 ^= arr[i]                                                                #Most Optimized solution o(N)
#     xor1 ^= (i + 1)
# xor1 ^= n
# print(xor1 ^ xor2)






# arr=[1,1,1,1,0,1,1,1,0,1,1,1,0,1,1]
# maxi=0
# count=0
# for i in range (len(arr)):                                                         # Find the maximum consecutive one
#     if arr[i]==1:
#         count+=1
#         maxi=max(maxi,count)
#     else:
#         count=0
# print(maxi)




# arr=[1,1,2,3,3,4,4]
# for i in range (len(arr)):
#     count=0
#     num=arr[i]
#     for j in range (len(arr)):
#         if arr[j]==num:
#             count+=1
#     if count == 1:
#         single=num
# print(single)




# arr=[1,1,2,3,3,4,4]
# # print(max(arr))
# hash=[0]*(max(arr)+1)
# # print(hash)
# for i in range (len(arr)):                                                       # better approch but the not suitable for the 10^12 or 10^9 these are very large numbers
#     hash[arr[i]]+=1
# print(hash)
# for i  in range (1,len(hash)):
#     if hash[arr[i]] == 1:
#         num=arr[i]
# print(num)







# arr=[1,1,2,3,3,4,4]
# freq={}
# for num in arr:                                                                       # optimal approch
#     if num in freq:
#         freq[arr[num]]+=1
#     else:
#         freq[arr[num]]=1
# print(freq)
# for key in freq:
#     if freq[key]==1:
#         print(key)
#         break




# arr=[1,1,2,3,3,4,4]
# xor=0
# for i in range (len(arr)):                                                           # Most optimal approch
#     xor = xor ^ arr[i]
# print(xor)




# arr=[1,2,3,1,1,1,1,4,2,3]
# d=3
# length=0
# for i in range (0,len(arr)):                                                       # Sum of subarray brutte force O(n^3)
#     for j in range (i,len(arr)):
#         sum=0
#         for k in range (i,j+1):
#             sum+=arr[k]
#         if sum == d:
#             length=max(length,j-i+1)
# print(length)




# arr=[1,2,3,1,1,1,1,4,2,3]
# d=3
# length=0
# for i in range (0,len(arr)): 
#     sum=0                                                      # Sum of subarray brutte force O(n^2)
#     for j in range (i,len(arr)):
#         sum+=arr[j]
#         if sum == d:
#             length=max(length,j-i+1)
# print(length)




# arr = [1,2,3,1,1,1,1,3,3]
# k = 6
# i=0
# length=0
# sum=0
# for r in range (len(arr)):                                                      # Optimal approch but only for the positive numbers
#     sum+=arr[r]
#     while sum > k:
#         sum-=arr[i]
#         i+=1
#     if sum==k:
#         length=max(length,r-i+1)
# print(length)




                                                                     # for negative ,positive and zeros use prefi+hashmap apporch (Remaining to do)




# arr=[2,6,5,8,11]
# Target=19
# Found=False
# for i in range (len(arr)):
#     for j in range (i+1,len(arr)):                                                     # 2 SUM Brute force approch
#         if arr[i]+arr[j]==Target:
#             Found=True
#             break
# if Found==True:
#     print("Found")
# else:
#     print("Not Found")






# arr=[2,6,5,8,11]
# Target=14
# freq={}
# for i in range(len(arr)):                                                   # Better approch of 2 SUM (using Hashing)
#     rem=Target-arr[i]
#     if rem in freq:
#         print(freq[rem],i)
#         break
#     freq[arr[i]]=i
# print(freq)






# arr=[2,6,5,8,11]
# Target=14
# left=0
# right=len(arr)-1
# arr.sort()
# while left < right:
#     s=arr[left]+arr[right]                                               # Two pointer approch of 2 SUM but it needs the array to be sorted
#     if s == Target:
#         print("Yes")
#         break
#     elif s < Target:
#         left+=1
#     else:
#         right-=1
    





# arr=[1,1,2,0,2,0,0,2,1,1,2,0,1,2,0,0,2,2,1,0]
# count0=0
# count1=0
# count2=0
# for i in range(len(arr)):
#     if arr[i]==0:count0+=1
#     elif arr[i]==1:count1+=1
#     else:count2+=1                                                             # sorting 0,1,2 only better approch brute approch is simply sorting
# print(count0)
# print(count1)
# print(count2)
# for i in range (0,count0):
#     arr[i]=0
# for i in range (count0,count0+count1):
#     arr[i]=1
# for i in range (count0+count1,len(arr)):
#     arr[i]=2
# print(arr)






# arr=[1,1,2,0,2,0,0,2,1,1,2,0,1,2,0,0,2,2,1,0]
# left=0
# mid=0
# high=len(arr)-1
# while mid<=high:
#     if arr[mid]==0:
#         arr[left],arr[mid]=arr[mid],arr[left]
#         left+=1
#         mid+=1
#     elif arr[mid]==1:                                                             # Dutch National Flag Algorithm (sorting 0,1,2)
#         mid+=1
#     else:
#         arr[mid],arr[high]=arr[high],arr[mid]
#         high-=1
# print(arr)




# arr=[2,2,3,3,1,2,2]
# for i in range (len(arr)):
#     count=0
#     for j in range (i,len(arr)):                                                  # Find Majority element greater then n/2
#         if arr[j]==arr[i]:  
#             count+=1
#         if count>len(arr)//2:
#             print(arr[i])
#             break
        




# arr=[2,2,3,3,1,2,2]
# Target=len(arr)//2
# freq={}
# for i in range (len(arr)):                                               # Better Approch
#     if arr[i] not in freq:
#         freq[arr[i]]=1
#     else:
#         freq[arr[i]]+=1

# for key,value in freq.items():
#     if value>Target:
#         print(key)
#         break





# arr=[2,2,3,3,1,2,2]
# candidate=None
# count=0
# for num in arr:
#     if count == 0:
#         candidate = num
#     if num == candidate:                                  # Morse voting algorithms to find the majority element from the array
#         count+=1
#     else:
#         count-=1
# # print(candidate)
# candidateCount=arr.count(candidate)
# if candidateCount > len(arr)//2:
#     print(candidate)
# else:
#     print("Candidate not found")

# Bubble sort



# def boubleSort(a):
#     n=len(a)
    
#     for i in range (len(a)):
#         swapped = False
#         for j in range(0,n-i-1):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#                 swapped = True
#         if not swapped :
#             break
#     return a

# a=[34,65,87,43,78,48,96,42,33,5,67,77]
# sorted_arr = boubleSort(a)
# print(sorted_arr,end=" ")







#   insersion Sort


# def insersionSort(a):
#     for i in range (1,len(a)):
#         key = a[i]
#         j = i-1

#         while j>=0 and key < a[j]:
#             a[j+1]=a[j]
#             j-=1
#             a[j+1]=key
#     return a


# a=[34,65,87,43,78,48,96,42,33,5,67,77]
# sorted_arr = insersionSort(a)
# print(sorted_arr,end=" ")






# selection sort




# def selectionSort(a):
#     n=len(a)
#     for i in range (n-1):
#         min = i
#         for j in range (i+1,n):
#             if a[j]<a[min]:
#                 min=j
#         a[i],a[min]=a[min],a[i]
#     return a


# a=[34,65,87,43,78,48,96,42,33,5,67,77]
# sorted_arr = selectionSort(a)
# print(sorted_arr,end=" ")







#    Merge sort


# def MergeSort(a,n):
#    if n>1:
#       m=n//2
#       l1=a[:m]
#       n1=len(l1)
#       l2=a[m:]
#       n2=len(l2)
#       MergeSort(l1,n1)
#       MergeSort(l2,n2)
#       i=j=k=0
#       while i<n1 and j<n2:
#          if l1[i]<l2[j]:
#             a[k]=l1[i]
#             i+=1
#          else:
#             l1[i]>l2[j]
#             a[k]=l2[j]
#             j+=1
#          k+=1
#       while i < n1:
#          a[k] = l1[i]
#          i = i + 1
#          k = k + 1    
#       while j < n2:
#          a[k]=l2[j]
#          j = j + 1
#          k = k + 1
#    return a
      
      
# a=[34,65,87,43,78,48,96,42,33,5,67,77]
# n=len(a)
# sorted_arr = MergeSort(a,n)
# print(sorted_arr,end=" ")







#     Quick sort




# def partition(a,low,high):
#     pivot = a[high]
#     i=low-1
#     for j in range(low, high):
#         if a[j] < pivot:
#             i += 1
#             swap(a, i, j)
#     swap(a, i + 1, high)
#     return i + 1

# def swap(a, i, j):
#     a[i], a[j] = a[j], a[i]


# def quickSort(a,low,high):
#     if low<high:
#         pi = partition(a,low,high)
#         quickSort(a,low,pi-1)
#         quickSort(a,pi+1,high)


# a=[34,65,87,43,78,48,96,42,33,5,67,77]
# n = len(a)

# quickSort(a, 0, n - 1)
    
# for val in a:
#     print(val, end=" ")
# arr=[2,7,11,15]
# Target=9
# class Solution :

#     def twoSum (self,arr,Target):
#         for i in range (len(arr)):
#             found=False
#             for j in range (i+1,len(arr)):                              #2 Sum
#                 if arr[i]+arr[j]==Target:
#                     return [i,j]
#         return []
                
# obj=Solution()
# res=obj.twoSum(arr,Target)
# print(res)





# class Solution():
#     def twoSum (self,arr,Target):
#         freq={}
#         for i in range (len(arr)):
#             rem=Target-arr[i]
#             if rem in freq:
#                 return [freq[rem],i]                          # 2 Sum
#             else :
#                 freq[arr[i]]=i
#         return []
# arr=[2,7,11,15]
# Target=9
# obj=Solution()
# res=obj.twoSum(arr,Target)
# print(res)





# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         left=1
        
#         n=len(nums)
#         for right in range(1,n):
#             if nums[right]!=nums[left-1]:                       # Remove Duplicate without using extra space
#                 nums[left]=nums[right] 
#                 left+=1
#         return left
        
# nums = [0,0,0,1,1,1,1,2,2,3,3,3,3,3,4]
# obj=Solution()
# res=obj.removeDuplicates(nums) 
# print(res)
# print(nums)






# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         left=0
#         for right in range (len(nums)):
            
#             if nums[right] != val:
#                 nums[left]=nums[right]
#                 left+=1
#         return left    
# nums=[3,2,2,3]
# val=3
# obj=Solution()
# res=obj.removeElement(nums,val)
# print(res)
# print(nums)





# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:
#         n=len(digits)
#         for i in range (n-1,-1,-1):
#             if digits[i]!=9:
#                 digits[i]+=1
#                 return digits
#             if digits[i]==9:
#                 digits[i]=0
#             if digits[0]==0:
#                 return [1]+digits

               
#         return digits
# digits=[1,2,3,9]
# obj=Solution()
# res=obj.plusOne(digits)
# print(res)





# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:
#         n=len(digits)
#         for i in range (n-1,-1,-1):
#             if digits[i]!=9:
#                 digits[i]+=1
#                 return digits
#             digits[i]=0
               
#         return digits
# digits=[1,2,3,9]
# obj=Solution()
# res=obj.plusOne(digits)
# print(res)





class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        left=m-1
        right=n-1
        k=m+n-1
        while left>=0 and right>=0:
            if nums2[right]>=nums1[left]:
                nums1[k]=nums2[right]
                right-=1
                k-=1
            else:
                nums1[k]=nums1[left]
                left-=1
                k-=1
        while right>=0:
            nums1[k]=nums2[right]
            k-=1
            right-=1

nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=len(nums1)
n=len(nums2)
m=m-n
obj=Solution()
res=obj.merge(nums1,m,nums2,n)
print(res)
print(nums1)
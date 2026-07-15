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






# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         left=m-1
#         right=n-1
#         k=m+n-1
#         while left>=0 and right>=0:
#             if nums2[right]>=nums1[left]:
#                 nums1[k]=nums2[right]
#                 right-=1
#                 k-=1
#             else:
#                 nums1[k]=nums1[left]
#                 left-=1
#                 k-=1
#         while right>=0:
#             nums1[k]=nums2[right]
#             k-=1
#             right-=1

# nums1=[1,2,3,0,0,0]
# nums2=[2,5,6]
# m=len(nums1)
# n=len(nums2)
# m=m-n
# obj=Solution()
# res=obj.merge(nums1,m,nums2,n)
# print(res)
# print(nums1)






# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#         for i in range (len(nums)):
#             if nums[i]>=target:
#                 return i
#         return len(nums)
            
# nums=[1,3,5,6]
# target=5
# obj=Solution()
# res=obj.searchInsert(nums,target)
# print(res)






# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#         n=len(nums)
#         i=0
#         j=n-1        
#         while i<=j:
#             mid=(i+j)//2
#             if nums[mid]==target:
#                 return mid
#             elif target<nums[mid]:
#                 j=mid-1
#             else:
#                 i=mid+1
#         return i
# nums=[1,3,5,6]
# target=0
# obj=Solution()
# res=obj.searchInsert(nums,target)
# print(res)






# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         freq={}
#         for num in nums:
#             if num not in freq:
#                 freq[num]=1
#             else:
#                 freq[num]+=1
#             if freq[num]==2:
#                 return True
#         return False
        
# nums=[1,2,3,4]
# obj=Solution()
# res=obj.containsDuplicate(nums)
# print(res)






# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False
        
# nums=[1,2,3,1]
# obj=Solution()
# res=obj.containsDuplicate(nums)
# print(res)






# class Solution:
#     def findMissingElements(self, nums: list[int]) -> list[int]:
#         n=len(nums)
#         total=0
#         sum=0
#         maxi=max(nums)
#         mini=min(nums)
#         for i in range (mini,maxi+1):
#             total+=i
#         for i in range (n):
#             sum+=nums[i]
#         if total==sum:
#             return []
#         return total-sum
        
# nums=[6,7,8,9]
# obj=Solution()
# res=obj.findMissingElements(nums)
# print(res)   






# class Solution:
#     def findMissingElements(self, nums: list[int]) -> list[int]:
#        res=set(nums)
#        ans=[]
       
#        for num in range (min(nums),max(nums)+1):
#             if num not in res:
#                ans.append(num)
#        return ans
           
        
# nums=[1,2,3,5]
# obj=Solution()
# res=obj.findMissingElements(nums)
# print(res) 







# class Solution:
#     def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
#         freq={}
#         for i in range (len(nums)):
#             if nums[i] in freq:
#                if abs(i-freq[nums[i]])<=k:
#                    return True
#             freq[nums[i]]=i
#         return False
        
        
# nums=[1,2,3,1]
# k=3
# obj=Solution()
# res=obj.containsNearbyDuplicate(nums,k)
# print(res) 





# class Solution:
#     def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
#         for i in range (len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j] and abs(i-j)<=k:
#                     return True
#         return False
        
        
# nums=[1,2,3,1]
# k=3
# obj=Solution()
# res=obj.containsNearbyDuplicate(nums,k)
# print(res) 




# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         i=0
#         j=0
#         while j<len(nums):
#             if nums[j]!=0:
#                 nums[i],nums[j]=nums[j],nums[i]
#                 j+=1
#                 i+=1
#             else:
#                 j+=1
#         return nums
            

# nums=[0,1,0,3,12]
# obj=Solution()
# res=obj.moveZeroes(nums)
# print(res)
 



# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         freq={}
#         m=len(nums)//2
#         for i in range (len(nums)):
#            if nums[i] not in freq:
#                freq[nums[i]]=1
#            else:
#                freq[nums[i]]+=1
#         for key,value in freq.items():
#             if value>m:
#                 return key
          
# nums=[1,1,2,2,3,3,3,3,3,3,3,3]
# obj=Solution()
# res=obj.majorityElement(nums)
# print(res)

        


# print(res)
 



# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         ele=None
#         count=0
#         for i in range (len(nums)):
#             if count==0:
#                 ele=nums[i]
#                 count=1
#             elif nums[i]==ele:
#                 count+=1
#             else:
#                 count-=1
#         count1=0
#         n=len(nums)//2
#         for i in range (len(nums)):
#             if nums[i]==ele:
#                 count1+=1
#         if count1>n:
#             return ele
#         return -1

          
# nums=[1,1,2,2,3,3,3,3,3,3,3,3]
# obj=Solution()
# res=obj.majorityElement(nums)
# print(res)



# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         freq={}
#         for i in range (len(nums)):
#             if nums[i] not in freq:
#                 freq[nums[i]]=1
#             else:
#                 freq[nums[i]]+=1
#         for key,value in freq.items():
#             if value==1:
#                 return key

# nums=[2,2,4,4,6]
# obj=Solution()
# res=obj.singleNumber(nums)
# print(res)   



# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         ans=0
#         for num in nums:
#             ans^=num
#         return ans
# nums=[2,2,4,4,6]
# obj=Solution()
# res=obj.singleNumber(nums)
# print(res)   



class Solution:

    def NcR(self,n,r):
        res=1
        for i in range (r):
            res=res*(n-i)
            res=res//(i+1)
        return res

    def generate(self, numRows: int) -> list[list[int]]:
        
        total=[]
        for row in range (numRows):
            res=[]
            for col in range (row+1):
                res.append(self.NcR(row,col))
            total.append(res)
        return total

numRows=6       
obj=Solution()
res=obj.generate(numRows)
print(res)   



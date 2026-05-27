# def find_sum(n):
#     total = 0
#     while n>0 :
#         total+=n%10
#         n=n//10                                                        sum of the degits 
#     return total
# N = int(input("Enter the number: "))
# print(find_sum(N)) 






# def Palindrome(n):
#    original=n
#    reverse = 0
#    while n>0:
#       digit = n%10
#       reverse=reverse*10+digit
#       n=n//10
#    return original == reverse
# N = int(input("Enter the number: "))
# if Palindrome(N):
#     print("It is a palindrome")
# else:
#     print("It is not a Palindrome")




# def vowel_count(n):
#     count=0
#     vowels="aeiou"
#     for ch in n:
#         if ch in vowels:
#             count+=1
#     return count
# N = input("Enter the number: ")
# print(f"vowels count is : {vowel_count(N)}")



# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# N = int(input("Enter the number: "))
# print("Factorial:", factorial(N))






# def fibo(n):
#     a = 0
#     b = 1
    
#     for i in range(n):
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
# N = int(input("Enter the number: "))
# print("Fibonacci series:", end=" ")
# fibo(N)



# def is_prime(n):
#     if n <= 1:
#         return False
    
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
    
#     return True
# N = int(input("Enter the number: "))
# if is_prime(N):
#     print('yes it is a prime number')
# else:
#     print("no its not a prime number")






# def reverse(s):
#     words = s.split()
#     reverse_Str = []
#     for i in range (len(words)-1,-1,-1):
#         reverse_Str.append(words[i])

#     return " ".join(reverse_Str)
# N = (input("Enter the string: "))
# reve = reverse(N)
# print(reve)








# def second(n):
#     first = second = float("-inf")
    
#     for num in n:
#         if num > first:
#             second = first      # shift
#             first = num
#         elif num > second and num != first:
#             second = num
    
#     return second   


# N = list(map(int, input("Enter the numbers: ").split()))
# result = second(N)
# print(result)





# def remove_duplicates(n):
#     result=[]
#     for num in n:
#         if num not in result:
#             result.append(num)

#     return result
# arr = list(map(int, input("Enter elements: ").split()))
# print("After removing duplicates:", remove_duplicates(arr))








# def count_frequency(arr):
#     freq={}
#     count = 0
#     for num in arr:
#         if num in freq:
#             freq[num]+=1
#         else:
#             freq[num] = 1

#     return freq

# arr = list(map(int, input("Enter elements: ").split()))
# result = count_frequency(arr)

# for key, value in result.items():
#     print(key, "→", value)







# def missing_number(arr, n):
#     total = n * (n + 1) // 2
#     actual = sum(arr)
#     return total - actual


# arr = list(map(int, input("Enter elements: ").split()))
# n = int(input("Enter n: "))
# print("Missing number:", missing_number(arr, n))





# def linear_search(arr, key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i   # return index
#     return -1


# arr = list(map(int, input("Enter elements: ").split()))
# key = int(input("Enter element to search: "))

# result = linear_search(arr, key)

# if result != -1:
#     print("Element found at index:", result)
# else:
#     print("Element not found")




# def is_armstrong(n):
#     num = n
#     power = len(str(n))
#     total = 0

#     while n > 0:
#         digit = n % 10
#         total += digit ** power
#         n = n // 10

#     return total == num


# N = int(input("Enter number: "))

# if is_armstrong(N):
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")









# def evenOddSum(n):
#     even=[]
#     odd=[]
#     for num in n:
#         if num%2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
    
#     return even,odd
            


# arr = list(map(int, input("Enter elements: ").split()))
# even, odd = evenOddSum(arr)
# print("Even numbers:", even)
# print("Odd numbers:", odd)








# print("hello world")



# print((input("what is your name?")))



# a=int(input("what is your number?"))
# b=int(input("what is your second number?"))
# c=a+b
# print("the sum of the two numbers is",c)





# a=int(input("what is your number?"))
# b=int(input("what is your second number?"))
# o=(input("what is your operation ( +,-,*,/ )?"))
# if o=="+":
#     print(a+b)
# elif o=="-":
#     print(a-b)
# elif o=="*":
#     print(a*b)
# elif o=="/":
#     print(a/b)
# else:
#     print("Invalid input")




# a=int(input("what is your number?"))
# b=int(input("what is your second number?"))
# o=(input("what is your operation ( +,-,*,/ )?"))
# operation=f"{a}{o}{b}"
# print(eval(operation))





# a=int(input("what is your number?"))
# if a<0 :
#     print("It is a negative number")
# elif a>0:
#     print("It is a positive number")
# else:
#     print("The number is zero")    





# a=int(input("what is your number?"))
# b=int(input("what is your second number?"))
# c=int(input("what is your third number?"))
# if a>b and a>c:
#     print("a is greater")
# elif b>c:
#     print("b is greater")
# else:
#     print("c is greater")




# a=int(input("what is your number?"))
# sum = 0
# for i in range(1,a+1):
#     sum += i
# print("the sum of the first",a,"numbers is",sum)





# a=(input("what is your number?"))
# count = 0
# for i in range(a):
#     count += 1
# print("the count of the first numbers is",count)






# a=int(input("what is your number?"))
# reversedNumber = 0
# while a>0:
#     digit = a % 10
#     reversedNumber = (reversedNumber * 10) + digit
#     a //= 10
# print("The reversed number is:", reversedNumber)







# def reverse_number(n):
#     reversedNumber = 0
#     t=n
#     while t>0:
#      digit = t % 10
#      reversedNumber = (reversedNumber * 10) + digit
#      t //= 10
#     return(reversedNumber)
   
# a=int(input("Enter the number : "))
# b=reverse_number(a)
# if a==b:
#     print("It is an palindrome")
# else:
#     print("Its not an palindrome")





# p=int(input("Enter a number:"))
# a,b = 0,1
# print("Fibonacci sequence:")
# for i in range(p):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c





# def reverse_number(n):
#     count = 0
   
#     t=n
#     while t>0:
#      digit = t % 10
#      cubeing = digit**3
#      count+=cubeing
#      t //= 10
#     return(count)
   
# a=int(input("Enter the number : "))
# b=reverse_number(a)
# if a==b:
#     print("It is an Anagram")
# else:
#     print("Its not an Anagram")





# a = int(input("Enter the number: "))

# if a <= 1:
#     print(f"{a} is not a prime number.")
# else:
#     is_prime = True
#     for i in range(2, int(a**0.5) + 1):
#         if a % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(f"{a} is a prime number.")
#     else:
#         print(f"{a} is not a prime number.")






# def get_gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# # Example usage:
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print(f"The GCD of {num1} and {num2} is: {get_gcd(num1, num2)}")






#Arrays



# a=[30,23,34,56,44,78,43,33]
# largest=a[0]
# for i in range(1,len(a)):
#     if a[i]>largest:
#         largest=a[i]
   

# print(largest)







# a=[30,23,34,56,44,78,43,33]
# smallest=a[0]
# for i in range(1,len(a)):
#     if a[i]<smallest:
#         smallest=a[i]
   
# print(smallest)







# a=[2,2,2,2,2,2,2,2,2,2]
# sum=0
# for i in range (0,len(a)):
#     sum+=a[i]

# print(sum)   




# a=[23,45,43,47,87,42,76,89,67]
# num=43
# for i in range (0,len(a)):
#     if a[i]==num:
#         print(f"Print number found at index {i}")








# a=[30,23,34,56,44,78,43,33]
# b=[]
# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])
   
# print(b)






# a=[30,23,34,56,44,78,43,33]
# even=0
# odd=0
# for i in range(0,len(a)):
#     if a[i]%2 == 0:
#         even+=1
#     else:
#         odd+=1

# print(f"even = {even} and odd = {odd}")









# a = [30, 23, 34, 56, 44, 78, 43, 33]

# min_val = a[0]
# max_val = a[0]

# # Single traversal
# for i in range(1, len(a)):
#     if a[i] > max_val:
#         max_val = a[i]
#     elif a[i] < min_val:
#         min_val = a[i]

# print(f"Min: {min_val}, Max: {max_val}")









#strings







# str1 = "hello world"
# reverse=""
# for char in str1:
#     reverse = char+reverse
# print(reverse)






# str1 = "madam"
# reverse=""
# for char in str1:
#     reverse = char+reverse
# if str1==reverse:
#     print("palindrome")
# else:
#     print("not a palindrome")







# str1 = "madam"
# vol="a,e,i,o,u"
# vowel=0
# consonant=0
# for char in str1:
#     if char in vol:
#         vowel+=1
#     else:
#         consonant+=1

# print(vowel)
# print(consonant)








# a=input("Enter the sentence here : ")
# sentence = a
# count=0
# in_word=False
# for char in sentence:
#    if char != " ":
#       if not in_word:
#          count+=1
#          in_word=True
#    else:
#       in_word=False

# print(count)










# s="banana"
# frequency={}
# for char in s:
#     if char not in frequency:
#         frequency[char] = 1
#     else:
#         frequency[char] += 1

# for char,count in frequency.items():
#      print(f"{char} : {count}")










# s="banana"
# frequency={}
# for char in s:
#     if char not in frequency:
#         frequency[char] = 1
#     else:
#         frequency[char] += 1

# non_repeating=None
# for char in s:
#     if frequency[char]==1:
#       non_repeating=char
#     break 

# if non_repeating :
#     print(f"the first non repeating char is {non_repeating}")
# else:
#     print("Not found")












# s="aaabbcccc"
# frequency={}
# for char in s:
#     if char not in frequency:
#         frequency[char] = 1
#     else:
#         frequency[char] += 1

# for char,count in frequency.items():
#      print(f"{char}{count}", end="")












# s="aaabbccccd"
# frequency={}
# for char in s:
#     if char not in frequency:
#         frequency[char] = 1


# for char in frequency:
#      print(f"{char}", end="")










# word1 = "listen"
# word2 = "silent"

# if sorted(word1) == sorted(word2):
#     print("It is an anagram")
# else:
#     print("No, not an anagram")


# def is_anagram(word1, word2):
#     if len(word1) != len(word2):
#         return False
    
#     count = {}
    
#     # Count chars in word1
#     for char in word1:
#         count[char] = count.get(char, 0) + 1
        
#     # Subtract chars in word2
#     for char in word2:
#         if char not in count:
#             return False
#         count[char] -= 1
#         if count[char] < 0:
#             return False
            
#     return True

# print(is_anagram("listen", "silent")) # True









# word="kya bolti public"
# splited = word.split(" ")
# print(splited)
# for i in range(len(splited)-1,-1,-1):
#     print(splited[i],end=" ")






#recurrsion








# def count(current, n):
#     if current > n:
#        return

#     print(current,end=" ")
#     count(current+1,n)
# n=int(input("Enter the number"))
# print(count(1,n))







# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
    
#     return n*factorial(n-1)
# n=int(input("Enter the number"))
# print(factorial(n))










# def sum(current,n):
#     if current>n:
#         return 0
#     return current+sum(current+1,n)



# n=int(input("Enter the number"))
# print(sum(1,n))












# def reverse_string(s):
#     if len(s) <= 1:
#         return 0
#     return s[-1]+ reverse_string(s[:-1])
        
# input_str = "hello"
# print(f"Original: {input_str}")
# print(f"Reversed: {reverse_string(input_str)}")



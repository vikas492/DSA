# print("hello world")


# name = "Vikas"
# age = 20

# print("My name is", name)
# print("I am", age, "years old")
 
# print(f"My name is {name} and I am {age} years old")          f strings

# a = 3
# b = 2

# print(a + b)  # 15
# print(a - b)  # 5
# print(a * b)  # 50
# print(a / b)  # 2.0
# print(a % b)   # Modulus → remainder → 0
# print(a ** 2)  # Power → 100
# print(a // b)  # Floor division → 2
# x = 10
# y = 5

# print(x > y)   # True
# print(x < y)   # False
# print(x == y)  # False
# print(x != y)  # True
# a = True
# b = False

# print(a and b)  # False
# print(a or b)   # True
# print(not a)    # False

# print(2 + 3 * 4)  # 14 (not 20)
# print(10 > 5 and 5 > 2)


# age = 16

# if age >= 18:
#     print("Can vote")
# else:
#     print("Cannot vote")



# marks = 75

# if marks >= 90:
#     print("A Grade")
# elif marks >= 60:
#     print("B Grade")
# else:
#     print("Fail")



# age = 20

# if age >= 18:
#     if age >= 21:
#         print("Can drink")
#     else:
#         print("Only voting allowed")




# i = 1

# while i <= 5:
#     print(i)          while loop runs until the condition becomes false
#     i += 1




# for i in range(5):           fro loop runs for a specific number of iterations   
#     print(i)

# range(5)        # 0 to 4
# range(1, 6)     # 1 to 5                 note this is very important
# range(1, 10, 2) # 1,3,5,7,9



# def calculate_bill(price, quantity):
#     total = price * quantity
#     return total

# print(calculate_bill(100, 3))


# with open("myfile.txt", "x") as file:
#     file.write("Created new file")

# with open("myfile.txt", "w") as file:
#     file.write("Hello Vikas")

# with open("myfile.txt", "a") as file:
#     file.write("thik he hoga\n")

# with open("myfile.txt", "r") as file:
#     content = file.read()
    # print(content)




# try:
#     num = int(input("Enter number: "))
#     print(10 / num)

# except:
#     print("Error occurred")

# else:
#     print("Success")



# class Bank:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         self.balance -= amount


# # Create object
# bank1 = Bank(1000)

# # Use methods
# bank1.deposit(500)
# bank1.withdraw(200)

# print(bank1.balance)



# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# print(fibo(6)) 
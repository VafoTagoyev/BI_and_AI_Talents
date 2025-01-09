# 1. Write a program that accepts a username and password and checks if both are not empty.

username = input("Enter username: ")
password = input("Enter password: ")
if username == "":
    print("Username cannot be blank")
elif password == "":
    print("Password cannot be blank")
else:
    print("Login successful")

# 2. Create a program that checks if two numbers are equal and outputs a message if they are.

a, b = map(int, input().split())
if a == b:
    print("Numbers are equal")
else:
    print("Numbers are not equal")

# 3. Write a program that checks if a number is positive and even.

n = int(input("Enter a number: "))
if n > 0 and n % 2 == 0:
    print("Number is positive and even.")

# 4. Write a program that takes three numbers and checks if all of them are different.

a, b, c = map(int, input().split())
if a != b and a != c and b != c:
    print("YES")

# 5. Create a program that accepts two strings and checks if they have the same length.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) == len(s2):
    print("Length of strings equal")

# 6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.

n = int(input("Enter a number: "))
if n % 15 == 0:
    print("FizzBuzz")

# 7. Write a program that checks if the sum of two numbers is greater than 50.8.

a, b = map(float, input().split())
if a + b > 50.8:
    print("Yes")

# 8. Create a program that checks if a given number is between 10 and 20 (inclusive)

n = int(input("Enter a number: "))
if 10 <= n <= 20:
    print("Yes")
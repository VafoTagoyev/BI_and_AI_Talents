# 1. Create a program that takes a float number as input and rounds it to 2 decimal places.

print(round(float(input("Enter number: ")), 2))

# 2. Write a Python file that asks for three numbers and outputs the largest and smallest.

a, b, c = map(int,(input().split()))
print('Largest:', max(a, b, c))
print('Smallest:', min(a, b, c))

# 3. Create a program that converts kilometers to meters and centimeters.

km = float(input("Enter in kilometers: "))
m = int(km * 1000)
cm = int(m * 100)
print(f"{km} km is {m} in meters and {cm} in centimeters")

# 4. Write a program that takes two numbers and prints out the result of integer division and the remainder.

a, b = map(int, input().split())
print(f"Integer division: {a // b}, remainder: {a % b}")

# 5. Make a program that converts a given Celsius temperature to Fahrenheit.

celsius = float(input("Celsius: "))
print(f"{celsius} Celsius is {celsius * 1.8 + 32} in Fahrenheit")

# 6. Create a program that accepts a number and returns the last digit of that number.

n = int(input("Enter a number: "))
print(f"The last digit of {n} is {n % 10}")

# 7. Create a program that takes a number and checks if it’s even or not.

n = int(input("Enter a number: "))
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")
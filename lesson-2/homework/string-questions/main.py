# 1. Create a program to ask name and year of birth from user and tell them their age.

name = input("What is your name? ")
birth_year = int(input("What is your birth year? "))
print(f"{name}, you are {2025 - birth_year} years old.")

# 2. Extract car names from this text: txt = 'LMaasleitbtui'

txt = "LMaasleitbtui"
car_names = ["Lacetti", "Malibu", "Matiz", "Spark", "Nexia"]
extracted_cars = [car for car in car_names if car.lower() in txt.lower()]
print(extracted_cars)

# 3. Write a Python program to:
        # Take a string input from the user.
        # Print the length of the string.
        # Convert the string to uppercase and lowercase.

s = input("Enter a string: ")
print(f"Length of {s} is {len(s)}")
print(f"Uppercase: {s.upper()}, Lowercase: {s.lower()}")

# 4. Write a Python program to check if a given string is palindrome or not.

s = input("Enter a string: ")
if s[::-1] == s:
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")

# 5. Write a program that counts the number of vowels and consonants in a given string.

s = input("Enter a string: ")
vowels = set('aeiou')
vowel_count = 0
consonant_count = 0

for char in s:
    if char.isalpha():
        if char.lower() in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Number of vowels: {vowel_count}, Number of consonants: {consonant_count}")

# 6. Write a Python program to check if one string contains another.

s1 = input("Enter a string: ")
s2 = input("Enter another string: ")
if s2 in s1:
    print(f"{s2} is in {s1}")
else:
    print(f"{s2} is not in {s1}")

# 7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.

sentence = input("Enter a sentence: ")
replace_with = input("Enter a replace word: ")
replace_word = input(f"Enter a word to replace with {replace_with}: ")
if replace_with in sentence:
    print(sentence.replace(replace_with, replace_word))
else:
    print("Word you entered doesn't exist")

# 8. Write a program that asks the user for a string and prints the first and last characters of the string.

s = input("Enter a string: ")
print(s[0])
print(s[-1])

# 9. Ask the user for a string and print the reversed version of it.

s = input("Enter a string: ")
print(s[::-1])

# 10. Write a program that asks the user for a sentence and prints the number of words in it.

sentence = input("Enter a sentence: ")
print(len(sentence.split()))

# 11. Write a program to check if a string contains any digits.

s = input("Enter a string: ")
if any(char.isdigit() for char in s):
    print(f"String contains digits")
else:
    print(f"String does not contain digits")

# 12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., - or ,).

words = input("Enter words seperated by space: ").split()
print('-'.join(words))

# 13. Ask the user for a string and remove all spaces from it.

print(input("Enter a string: ").replace(" ", ""))

# 14. Write a program to ask for two strings and check if they are equal or not.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if s1 == s2:
    print("Strings are same")
else:
    print("Strings are different")

# 15. Ask the user for a sentence and create an acronym from the first letters of each word.

words = input("Enter a sentence: ").split()
print(''.join(word[0].upper() for word in words if word.isalpha()))

# 16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.

s = input("Enter a string: ")
ch = input("Enter a character: ")
if len(ch) != 1:
    print("Invalid character")
else:
    print(s.replace(ch, ""))

# 17. Ask the user for a string and replace all the vowels with a symbol (e.g., *).

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
print(''.join("*" if char in vowels else char for char in s))

# 18. Write a program that checks if a string starts with one word and ends with another.

words = input("Enter a string: ").split()
if len(words) > 1:
    print(words[0])
    print(words[-1])
else:
    print("You entered one word")

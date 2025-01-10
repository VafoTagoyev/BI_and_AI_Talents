# 1. Return uncommon elements of lists. Order of elements does not matter.

list1 = [1, 1, 2]
list2 = [2, 3, 4]

uncommon_elements = []

for elem in list1:
    if elem not in list2:
        uncommon_elements.append(elem)

for elem in list2:
    if elem not in list1:
        uncommon_elements.append(elem)

print(uncommon_elements)

# 2. Print the square of each number which is less than n on a separate line.

n = 5

for i in range(1, n):
    print(i * i)

# 3. txt nomli string saqlovchi o'zgaruvchi berilgan. txtdagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.

txt = 'abcabcdabcdeabcdefabcdefg'
done = "aeiou"
counter = 0
ans = []

for i in range(len(txt)):
    counter += 1
    ans.append(txt[i])
    if i!=len(txt)-1 and counter >= 3 and txt[i] not in done:
        done += txt[i]
        ans.append('_')
        counter = 0

print(''.join(ans))

# 4. Number Guessing Game Create a simple number guessing game.

import random

def start_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"Try to guess the number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You guessed it right!")
            break
    else:
        print(f"You lost. The correct number was {number}.")

    play_again = input("Want to play again? (Y/N): ").strip().lower()
    if play_again in ['y', 'yes', 'ok']:
        start_game()
    else:
        print("Thanks for playing! Goodbye!")

start_game()

# 5. Password Checker Task: Create a simple password checker.

password = input("Enter a password: ")

if len(password) < 8:
    print("Password is too short.")
elif not any(char.isupper() for char in password):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")

# 6. Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Prime numbers between 1 and 100:")
for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ")

# Bonus. Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.

import random

def play_rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    winning_score = 5

    print("Welcome to Rock, Paper, Scissors!")
    print("First to 5 points wins the match!")

    while player_score < winning_score and computer_score < winning_score:
        computer_choice = random.choice(options)
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in options:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score: Player {player_score} - {computer_score} Computer\n")

    if player_score == winning_score:
        print("Congratulations! You won the match!")
    else:
        print("Computer wins the match. Better luck next time!")

play_rock_paper_scissors()
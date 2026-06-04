#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay
print("MasterMind")

import random
import hashlib

# Credentials are stored as hashes so the plain text values are not visible directly in the source.
USERNAME_HASH = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918" # hash for "admin"
PASSWORD_HASH = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8" # hash for "password"

def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()


def generate_Code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    # Count whites by subtracting black and calculating min digit frequency match
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
    return black_Pegs, white_Pegs

def show_Secret(mystery):
    print(mystery)

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is from 1 to 6. You have 10 attempts.")
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        while not valid_Guess:
            guess = input(f"Attempt {attempt}: ").strip()
            if guess.lower() == "login":
                login()
                continue
            if guess.lower() == "cheat":
                if isLogedIn:
                    show_Secret(secret_Code)
                else:
                    print("Login eerst met 'login' om 'cheat' te gebruiken.")
                continue
            if len(guess) == 4 and all(c in "123456" for c in guess):
                break
            print("Invalid input. Enter 4 digits, each from 1 to 6.")

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")

def login():
    global isLogedIn
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if hash_text(username) == USERNAME_HASH and hash_text(password) == PASSWORD_HASH:
        isLogedIn = True
        print("Login successful!")
    else:
        print("Login failed. Incorrect username or password.")


if __name__ == "__main__":
    isLogedIn = False
    again = 'Y'
    while again == 'Y' :
        play_Mastermind()
        again  = input (f"Play again (Y/N) ?").upper()


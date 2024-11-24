import time
import random

def guess():
    emoji_to_guess = random.shuffle("🗿", "💀")
    attempts = 0

    print("hello there and would wanna guess some emojis?")
    time.sleep(3)
    print("there are two emojis you have to pick its either this: 🗿, or this one: 💀")
    time.sleep(1)

    while True:
        try:
            user_guess = str(input("insert your emoji"))
        except:
            print("you must insert those following emojis using win + . ")
            continue

        attempts +=1

        if not user_guess == emoji_to_guess:
            print("Probably other one?")
        elif user_guess == emoji_to_guess:
            print(f"nice one you have guessed {emoji_to_guess} in a {attempts} try")

guess()
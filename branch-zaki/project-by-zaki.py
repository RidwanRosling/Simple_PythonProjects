import time
import random

emojis = ["💀", "🗿", "✅", "❌"]

def guess():
    emoji_to_guess = random.choice(emojis)
    attempts = 0

    print("hello there and would wanna guess some emojis?")
    time.sleep(3)
    print("there are two emojis you have to pick between this emojis: 💀, 🗿, ✅, ❌")
    time.sleep(2)
    print("go ahead and take a guess")
    time.sleep(1)

    while True:
        user_guess = str(input("insert your emoji: "))

        attempts +=1

        if not user_guess == emoji_to_guess:
            print("i think you guess the wrong one")
            time.sleep(1)
            print("note: use= win + . | to insert an emoji")
        elif user_guess == emoji_to_guess:
            print(f"nice one you have guessed {emoji_to_guess} in {attempts} try")
            break

guess()
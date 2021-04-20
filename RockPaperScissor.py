import math
import random

def main():
    rpc = ["rock", "paper", "scissor"]
    comphand = random.choice(rpc)
    print(comphand)
    userhand = input("Enter:").lower()
    if userhand in rpc:
        if comphand == userhand:
            print("Draw!")
        elif (comphand=="rock" and userhand == "paper") or (comphand=="paper" and userhand == "scissor") or (comphand=="scissor" and userhand == "rock"):
            print("You win!")
        else:
            print("You lose...")
    else:
        print("Enter a valid hand")

if __name__ == "__main__":
    main()
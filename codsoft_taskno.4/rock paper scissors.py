import random

print("----Welcome to Rock, Paper, Scissors!----")
user_score = 0
computer_score = 0
round_count = 1
while True:
    print(f"\nRound {round_count}")
    user = input("Choose rock, paper or scissors: ").lower().strip()

    while user not in ["rock", "paper", "scissors"]:
        print("Hmm... that's not a valid choice.")
        user = input("Try again (rock/paper/scissors): ").lower().strip()

    computer = random.choice(["rock", "paper", "scissors"])
    print(f"You picked: {user}")
    print(f"Computer picked: {computer}")
    if user == computer:
        print("It's a tie this round!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win this one!")
        user_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1
    print(f"Current score - You: {user_score} | Computer: {computer_score}")

    a= input("Wanna play another round? (yes/no): ").lower().strip()
    if a not in ["yes", "y"]:
        break
    round_count += 1

print("\nGame over!")
print(f"Final score - You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("Woohoo! You won the game")
elif computer_score > user_score:
    print("Ah,the computer won this time. You'll get it next time!")
else:
    print("It's a draw! Great game.")

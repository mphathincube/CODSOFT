import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

art = [rock, paper, scissors]

player_choice = int(input("Enter 0 for rock,1 for paper or 2 for scissors "))

if 0 > player_choice or player_choice > 2:
    print("❌please enter a number between 0 and 2")

else:
    print("player choice:")
    print(art[player_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(art[computer_choice])

    if player_choice == computer_choice:
        print("It's a draw")

    elif player_choice == 0 and computer_choice == 2:
        print("You Won🏆")

    elif player_choice == 1 and computer_choice == 0:
        print("You Won🏆")

    elif player_choice == 2 and computer_choice == 1:
        print("You Won🏆")
    elif player_choice >= 3:
        print("Enter a valid number")

    else:
        print("You lose😢")


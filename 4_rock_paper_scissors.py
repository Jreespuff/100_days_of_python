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

player_score = 0
computer_score = 0

img = [rock, paper, scissors]
name = ["rock", "paper", "scissors"]

while True:
    player_input = input("Choose 0 for Rock, 1 for paper, 2 for Scissors. Type q to quit. \n" ).lower()
    computer_input = random.randint(0,2)

    if player_input == 'q':
        print('Thanks for playing!')
        break
    else:
        player_input = int(player_input)

    print(f'You chose {name[player_input]} \n {img[player_input]}')

    print(f'Computer chose {name[computer_input]} \n {img[computer_input]}')



    if player_input == 0 and computer_input == 2:
        print("You Win!")
        player_score +=1
    elif player_input == 1 and computer_input == 0:
        print("You win!")
        player_score +=1
    elif player_input == 2 and computer_input == 1:
        print("You win!")
        player_score +=1
    elif player_input == computer_input:
        print('Draw!')
    else:
        print("You lose!")
        computer_score +=1

total_games = player_score + computer_score
winrate = round((player_score/total_games) * 100,2)

print(f'You won {player_score} times and the computer won {computer_score} times.')
print(f'Your win rate was {winrate} %.')


# ht = random.randint(0,1)
# if ht == 0:
#     print("heads")
# else:
#     print('tails')

# states_of_america = ["Deleware" , "Colorado", "Georgia"]
# print(states_of_america[0])
# print(states_of_america[-1]) #negative numbers starts from the end

# states_of_america.append("Jacobland") #add to the end of the list

# names_string = input("Enter the names of everybody, separated by commas: ")
# names = names_string.split(",")
# length = len(names)

# roll = random.randint(0,length - 1)

# paying = names[roll]
# print(f'{paying} is paying for the meal today.')

# Can also make a nested list. 
# fruits[pass]
# vegetables[pass]
# Dirty_dozen[fruits, vegetables]

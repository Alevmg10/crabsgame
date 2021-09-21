import random

# Crabs game

print("Be welcomed to the game of Crabs")
print("This game consists of 5 attempts, where you can either win or lose")

play = 5
new_bet = 0


def ask_bet():

    global new_bet

    new_bet = int(input("What will be your bet?: "))
    if new_bet < 1:
        print("Must be a number greater than zero '0'")
        return ask_bet()

# Block for throwing the dice.


def throw_dice():
    input('Pulse ENTER for throw the dice')

    a = random.randint(1, 6)
    b = random.randint(1, 6)

    return a + b

# Main game


def game(new_bet):

    dice = throw_dice()

    if dice == 7 or dice == 11:
        print("Dice show: ", dice, " Win ", new_bet, "!!")
        return new_bet
    elif dice == 2 or dice == 3 or dice == 12:
        print("Dice show: ", dice, "craps! You Lose")
        return -new_bet
    else:
        score = dice
        print()
        print("Score: ", score)

    # Second phase
    dice = throw_dice()

    print("Dice indicates: ", dice)

    while dice != 7 and dice != score:
        dice = throw_dice()
        print("Dice indicates: ", dice)

    if dice == 7:
        print("7 and OUT!! You Lose.")
    else:
        print(" You win the game ", new_bet)
        return new_bet


while play != 0:
    play -= 1
    ask_bet()
    game(new_bet)
    #play= int(input("To continue press  '0'. "))
    print("Game: ", play)

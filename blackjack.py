import random


def deal_cards():
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = random.choice(all_cards)
    return cards


def score(crds):
    if sum(crds) == 21 and len(crds) == 2:
        return 0
    if 11 in crds and sum(crds) > 21:
        crds.remove(11)
        crds.append(1)
    return sum(crds)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "its a draw"
    elif user_score == 0:
        return "you win"
    elif computer_score == 0:
        return "computer won"
    elif user_score == 21:
        return "you won"
    elif user_score > 21:
        return "you lost cause score exceeded"
    elif computer_score > 21:
        return "you won cause computer's score exceeded "
    elif user_score > computer_score:
        return "you won"
    else:
        return "you won"


user = []
computer = []
is_game_over = False
for _ in range(2):
    user.append(deal_cards())
    computer.append(deal_cards())
while not is_game_over:
    user_score = score(user)
    computer_score = score(computer)
    print(f"your cards {user} your score {user_score}")
    print(f"computers first card {computer[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        order = input("type 'y' to continue or 'n' to pass\n")
        if order == "y":
            user.append(deal_cards())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer.append(deal_cards())
    computer_score = score(computer)
print(f"your cards {user} your score {user_score}")
print(f"computer score is {computer_score} and cards is {computer}")
print(compare(user_score, computer_score))

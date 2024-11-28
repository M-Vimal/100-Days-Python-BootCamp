from  ascii_logo import game_title,vs
from data import higher_lower_data
import random

count = 0
def random_choice(datas):
    choosen = random.choices(datas,k=2)
    return choosen
def answer_check(option1,answer):
    global count
    if answer == 'a':
        if option1[0]['followers'] > option1[1]['followers']:
            count +=1
            return True
        else:return False

    if answer == 'b':
        if option1[0]['followers'] < option1[1]['followers']:
            count+=1
            return True
        else:return False

gamestart = False
print(game_title)

while not gamestart:
    option1 = random_choice(higher_lower_data)
    while option1[0] == option1[1]:
        option2 = random_choice(higher_lower_data)
    print(f"Compare A: {option1[0]['name'],option1[0]['description']}")
    print(vs)
    print(f"Against B: {option1[1]['name'],option1[1]['description']}")
    answer = input("who has more followers.Type 'A' or 'B' :")
    result = answer_check(option1=option1,answer=answer)
    print("\n" * 20)

    if result:
        print(game_title)
        print(f"you are correct your score is {count}")
    else:
        gamestart = True
        print(game_title)
        print(f"sorry that's wrong.your final score is {count}")



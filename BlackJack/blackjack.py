import random


def choose_card():
    numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(numbers)


def calculate_score(cards):
    score = sum(cards)
    # Adjust for Ace (11 -> 1) if score > 21
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


def startgame():
    print("Welcome to Blackjack!")
    play_again = True

    while play_again:
        # Initialize game variables
        user_cards = [choose_card(), choose_card()]
        computer_cards = [choose_card(), choose_card()]
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        game_over = False

        print("\nYour cards:", user_cards, "Current score:", user_score)
        print("Computer's first card:", computer_cards[0])

        # User's turn
        while not game_over:
            if user_score > 21:
                print("You bust! Computer wins!")
                game_over = True
                break

            take_card = input("Do you want another card? 'y' or 'n': ").lower()
            if take_card == 'y':
                user_cards.append(choose_card())
                user_score = calculate_score(user_cards)
                print("Your cards:", user_cards, "Current score:", user_score)
            else:
                game_over = True

        # Computer's turn
        while computer_score < 17:
            computer_cards.append(choose_card())
            computer_score = calculate_score(computer_cards)

        print("\nFinal Scores:")
        print("Your cards:", user_cards, "Final score:", user_score)
        print("Computer's cards:", computer_cards, "Final score:", computer_score)

        # Determine the winner
        if user_score > 21 and computer_score > 21:
            print("no one was win")
        elif user_score > 21:
            print("You bust! Computer wins!")
        elif computer_score > 21:
            print("Computer busts! You win!")
        elif user_score > computer_score:
            print("You win!")
        elif user_score < computer_score:
            print("Computer wins!")
        else:
            print("It's a draw!")

        # Replay option
        replay = input("\nDo you want to play again? 'y' or 'n': ").lower()
        if replay != 'y':
            play_again = False
            print("Thanks for playing!")
startgame()




# git remote add origin https://github.com/M-Vimal/100-Days-Python-BootCamp.git
# git branch -M main
# git push -u origin main
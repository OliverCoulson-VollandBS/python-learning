import random

def generate_card():
    card = random.randint(1, 10)
    print(card)
    return(card)
    
def calculate_score():
    score = 0
    card_pulled = generate_card()
    score = score + card_pulled
    card_pulled = generate_card()
    score = score + card_pulled
    return score

def player_turn(player_total_score):
    hitting_or_standing = True
    while hitting_or_standing == True:
            hit_or_stand = input("Hit or Stand?")
            if hit_or_stand == "hit":
                player_card_add = generate_card()
                player_total_score = player_total_score + player_card_add
                print(f"You are now on {player_total_score}")
                if player_total_score < 22:
                    hitting_or_stand_again = input("Would you like to hit again?")
                    if hitting_or_stand_again == "no":
                        hitting_or_standing = False
                        return player_total_score
                else:
                    print("Player busts!")
                    hitting_or_standing = False
                    return player_total_score
            else:
                hitting_or_standing = False
                return player_total_score


def dealer_turn(dealer_total_score):
    dealers_turn = True
    while dealers_turn == True:
        if dealer_total_score < 17:
            dealer_card_add = generate_card()
            dealer_total_score = dealer_total_score + dealer_card_add
            print(dealer_total_score)
        else:
            dealers_turn = False
            return dealer_total_score

def determine_winner(player_go, dealer_go):
    # If player more than dealer and not bust
    if player_go > dealer_go and player_go < 22:
        return "Player"
    # If player bust and dealer hasnt
    elif player_go > 22 and dealer_go < 22:
        return "Dealer"
    # If dealer and player same
    elif player_go == dealer_go:
        return "Both equal, push"
    # If dealer more than player and not bust
    elif player_go < dealer_go and dealer_go < 22:
        return "Dealer"
    # Player less than 22 and dealer bust
    elif player_go < 22 and dealer_go > 21:
        return "Player"
    else:
        return "Not covered yet"
        




print("Welcome to blackjack")
player_total_score = calculate_score()
dealer_total_score = calculate_score()
print(f"Player total score is {player_total_score}")
print(f"Dealer total score is {dealer_total_score}")

player_go = player_turn(player_total_score)
dealer_go = dealer_turn(dealer_total_score)

final_winner = determine_winner(player_go, dealer_go)
print(f"The winner is {final_winner}")
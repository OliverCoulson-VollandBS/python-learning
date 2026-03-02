import random

def bet(player_chips):
    bet_amount = input("How many chips do you want to bet?")
    bet_amount = int(bet_amount)
    player_chips = player_chips - bet_amount
    print(f"You've bet {bet_amount}, and have {player_chips} left.")
    return player_chips

def generate_card():
    card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    card = random.choice(card_list)
    if card in ["J", "Q", "K"]:
        value = 10
    elif card == "A":
        value = 11
    else:
        value = card
    print(card)
    return(value)
    
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
                if player_card_add == 11 and player_total_score > 21:
                    player_total_score = player_total_score - 10
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
            if dealer_card_add == 11 and dealer_total_score > 21:
                dealer_total_score = dealer_total_score - 10
            print(dealer_total_score)
        else:
            dealers_turn = False
            return dealer_total_score

def determine_winner(player_go, dealer_go, player_blackjack, dealer_blackjack):
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
    # Player blackjack and dealer not
    elif player_blackjack == True and dealer_blackjack == False:
        return "Player, with a blackjack!"
        # 2.5* chips
    else:
        return "Not covered yet"
        


playing = True
print("Welcome to blackjack")
player_chips = 100
while playing == True:
    player_blackjack = False
    dealer_blackjack = False

    player_chips = bet(player_chips)

    player_total_score = calculate_score()
    print(f"Player total score is {player_total_score}")

    if player_total_score == 21:
        print("Blackjack for Player!")
        player_blackjack = True

    player_go = player_turn(player_total_score)


    dealer_total_score = calculate_score()
    print(f"Dealer total score is {dealer_total_score}")

    if dealer_total_score == 21:
        print("Blackjack for Dealer!")
        dealer_blackjack = True

    dealer_go = dealer_turn(dealer_total_score)


    final_winner = determine_winner(player_go, dealer_go, player_blackjack, dealer_blackjack)
    print(f"The winner is {final_winner}")
    play_again = input("Would you like to play again?")
    if play_again == "No":
        playing = False
# Simple Blackjack

import random

def card_scoring(card1, card2, bet, player_chips):
    player_score = 0
    dealer_score = 0
    score = card1 + card2

    #if score == 1:
        #if card1 or card2 == range(10, 14):
            #score == 22
            #print("Blackjack!")
    #maybe not elif below
    if card1 == card2:
        print("Double!")
    if score == 11:
        double = print(input("Do you want to double?"))
        if double == "yes":
            double_card = random.randint(1, 13)
            score += double_card
            player_chips = player_chips - bet
            #Put here the decrease in the bet
    
    return score

def card_generator():
    player_face_card = False
    player_card1 = random.randint(1, 13)
    if player_card1 >= 10:
        player_face_card == True
    print(player_card1)

    player_card2 = random.randint(1, 13)
    if player_card2 >= 10:
        player_face_card == True
    print(player_card2)
    return (player_card1, player_card2)


player_chips = 100
playing = True
bet = 10
player_chips -= bet
    
while playing == True:
    print("Welcome to blackjack")

    player_cards = card_generator()
    print(player_cards)
    dealer_cards = card_generator()
    print(dealer_cards)

    player1_score = card_scoring(player_cards[0], player_cards[1], bet, player_chips)
    dealer_score = card_scoring(dealer_cards[0], dealer_cards[1], bet, player_chips)

    if player1_score > dealer_score:
        print(f"Player wins with {player1_score}!")
        player_chips == player_chips + bet * 2
    else:
        print(f"dealer wins with {dealer_score}")

    again = print(input("Do you want to play again?"))
    if again == "no":
        playing = False

    if player_chips <= 0:
        playing = False
        print("you've run out of chips")























# #def dealer_card_generator():
#     dealer_face_card = False
#     dealer_card1 = random.randint(1, 13)
#     if dealer_card1 >= 10:
#         dealer_face_card == True
#     print(dealer_card1)

#     dealer_face_card = False
#     dealer_card2 = random.randint(1, 13)
#     if dealer_card2 >= 10:
#         dealer_face_card == True
#     print(dealer_card2)

#     return(dealer_card1, dealer_card2)

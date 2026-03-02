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
    # if card1 == card2:
    #     print("Double!")
    # if score == 11:
    #     double = input("Do you want to double?")
    #     if double == "yes":
    #         double_card = random.randint(1, 13)
    #         score += double_card
    #         player_chips = player_chips - bet
    #         #Put here the decrease in the bet
    
    return score

def card_generator():
    player_face_card = False
    player_card1 = random.randint(1, 13)
    if player_card1 >= 10:
        player_face_card = True
    print(player_card1)

    player_card2 = random.randint(1, 13)
    if player_card2 >= 10:
        player_face_card = True
    print(player_card2)
    return (player_card1, player_card2)

#def card_3_onwards():

def hit_or_stand(player1_score, bust):
    sitting_or_standing = 1
    while sitting_or_standing == 1:
        hit_or_not = False
        card3 = 0
        hit_or_not = input("Hit or stand?")
        print(hit_or_not)
        if hit_or_not == "hit":
            card_3 = random.randint(1, 10)
            print(f"You got a {card_3}")
            player1_score = player1_score + card_3
            print(f"You're total score is now {player1_score}")
            if player1_score > 21:
                print("You've gone bust!")
                sitting_or_standing = 0
                bust = True
                print(bust)
                return bust
            else:
                hit_or_stand_again = input("Do you want to hit again?")
                if hit_or_stand_again == "no":
                    sitting_or_standing = 0
                else:
                    sitting_or_standing = 1
        else:
            print("You chose to stand")
            





player_chips = 100
playing = True
bet = 10
player_chips -= bet
    
while playing == True:
    bust = False
    print("Welcome to blackjack")

    player_cards = card_generator()
    print(player_cards)
    dealer_cards = card_generator()
    print(dealer_cards)

    player1_score = card_scoring(player_cards[0], player_cards[1], bet, player_chips)
    dealer_score = card_scoring(dealer_cards[0], dealer_cards[1], bet, player_chips)

    bust = hit_or_stand(player1_score, bust)
    print(bust)
    if bust == False:
        if player1_score > dealer_score:
            print(f"Player wins with {player1_score}!")
            player_chips = player_chips + bet * 2
        else:
            print(f"dealer wins with {dealer_score}")

        again = input("Do you want to play again?")
        if again == "no":
            playing = False

        if player_chips <= 0:
            playing = False
            print("you've run out of chips")
    else:
        again = input("Do you want to play again?")
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

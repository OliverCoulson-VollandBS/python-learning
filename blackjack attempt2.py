import random

def bet(player_chips):
    bet_amount = input("How many chips do you want to bet?")
    bet_amount = int(bet_amount)
    player_chips = player_chips - bet_amount
    print(f"You've bet {bet_amount}, and have {player_chips} left.")
    return player_chips, bet_amount

def generate_card(card_list):
    card = random.choice(card_list)
    card_list.remove(card)
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
    card_pulled = generate_card(card_list)
    score = score + card_pulled
    card_pulled = generate_card(card_list)
    if card_pulled == score:
        player_total_score = split(score, card_pulled)
    score = score + card_pulled
    if score == 11:
        player_total_score = double(score, player_chips, bet_amount)
    return score

def split(score, card_pulled):
    if dealer_playing == False:
        print("split!")
        global would_split
        would_split = input("Would you like to split?")
        if would_split == "yes":
            new_card = generate_card(card_list)
            score = score + new_card
            if new_card == 11 and score > 21:
                score = score - 10
                print(f"You are now on {score}")
                return score
            if score > 21:
                print("Player busts!")
                return score
        else:
            return score
    
def double(score, player_chips, bet_amount):
    print("Double!?")
    global would_double
    if dealer_playing == False:
        would_double = input("Would you like to double?")
        if would_double == "yes":
            new_card = generate_card(card_list)
            score = score + new_card
            player_chips = player_chips - bet_amount
            print(f"You are now on {score} and {player_chips} chips")
            if new_card == 11 and score > 21:
                score = score - 10
                print(f"You are now on {score}")
                return score
            if score > 21:
                print("Player busts!")
                return score
        else:
            return score



def player_turn(player_total_score):
    hitting_or_standing = True
    while hitting_or_standing == True:
        if player_total_score < 22:
            hit_or_stand = input("Hit or Stand?")
            if hit_or_stand == "hit":
                player_card_add = generate_card(card_list)
                player_total_score = player_total_score + player_card_add
                if player_card_add == 11 and player_total_score > 21:
                    player_total_score = player_total_score - 10
                print(f"You are now on {player_total_score}")
                #if player_total_score < 22:
                    # hitting_or_stand_again = input("Would you like to hit again?")
            else:
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
            dealer_card_add = generate_card(card_list)
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
    elif player_go >= 22 and dealer_go < 22:
        return "Dealer"
    # If dealer and player same
    elif player_go == dealer_go:
        return "Push"
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
        

card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", 
             "Q", "K", "A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 1, 2, 3, 4, 5, 6, 7, 
             8, 9, 10, "J", "Q", "K", "A"]
playing = True
print("Welcome to blackjack")
global player_chips
player_chips = 100
would_split = "no"
would_double = "no"
global bet_amount
while playing == True:
    dealer_playing = False
    player_blackjack = False
    dealer_blackjack = False

    player_chips, bet_amount = bet(player_chips)

    player_total_score = calculate_score()
    print(f"Player total score is {player_total_score}")

    if player_total_score == 21:
        print("Blackjack for Player!")
        player_blackjack = True

    if would_split == "no" and would_double == "no":
        player_go = player_turn(player_total_score)

    dealer_playing = True
    dealer_total_score = calculate_score()
    print(f"Dealer total score is {dealer_total_score}")

    if dealer_total_score == 21:
        print("Blackjack for Dealer!")
        dealer_blackjack = True

    dealer_go = dealer_turn(dealer_total_score)


    final_winner = determine_winner(player_go, dealer_go, player_blackjack, dealer_blackjack)
    print(f"The winner is {final_winner}")
    if final_winner == "Player":
        player_chips = player_chips + bet_amount * 2
        print(f"Congradulations, you win {bet_amount} chips!")
        if would_double == "yes":
            player_chips = player_chips + bet_amount
            print(f"Congradulations, you win {bet_amount * 2} chips!")
        if player_blackjack == "yes":
            player_chips = player_chips + bet_amount * 0.5
            print(f"Congradulations, you win {bet_amount * 2} chips!")
    if final_winner == "Push":
        player_chips = player_chips + bet_amount
        print("You get your chips back")
    play_again = input("Would you like to play again?")
    card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 
                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 
                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 
                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    if play_again == "no":
        playing = False
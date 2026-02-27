# blackjackgame?

# classes - dealer: has turn
# , player
import random

print("Welcome to blackjack")

dealer_chips_total = 0
total_chips = 0
# creates player class, and assigns their attributes
class Player():

  def __init__(self, card1, card2, chips):
    self.card1 = card1
    self.card2 = card2
    self.chips = chips

#only need to pass in self
  def player_result_fun(self):
    player_final_result = self.card1 + self.card2
    return player_final_result
  
  def chips_win(self):
    return total_chips == self.chips - 5

  def chips_loss(self):
    return total_chips == self.chips - 5

#assigns dealer class
class Dealer():

  def __init__(self, dealer_card1, dealer_card2, dealer_chips):
    self.dealer_card1 = dealer_card1
    self.dealer_card2 = dealer_card2
    self.dealer_chips = dealer_chips

  def dealer_result_fun(self):
    dealer_final_result = self.dealer_card1 + self.dealer_card2
    return dealer_final_result
  
  def dealer_chips_win(self):
    return dealer_chips_total == self.dealer_chips - 5

  def dealer_chips_loss(self):
    return dealer_chips_total == self.dealer_chips - 5

#temp results of random cards for player1
random_card1 = random.randint(1, 11)
random_card2 = random.randint(1, 11)

#temp results for dealer
dealer_random_card1 = random.randint(1, 11)
dealer_random_card2 = random.randint(1, 11)

# Creates the player and dealer from the blueprint
player1_object = Player(random_card1, random_card2, chips=5)
dealer_object = Dealer(dealer_random_card1, dealer_random_card2, dealer_chips=1000000)

#The main game
print("It is the players turn")
player1_go = player1_object.player_result_fun()
print(f"Player 1's got the cards {player1_go}")
print("It is the dealers turn")
dealer_go = dealer_object.dealer_result_fun()
print(f"The dealer got the cards {dealer_go}")
if player1_go >= dealer_go:
  print(f"The player wins with {player1_go} VS the dealers {dealer_go}!")
  player1_chips = player1_object.chips_win()
  dealer_chips = dealer_object.dealer_chips_loss()
  print(total_chips)
  print(dealer_chips_total)
else:
  print(f"The dealer wins with {dealer_go} VS the players {player1_go}!")
  player1_chips = player1_object.chips_loss()
  dealer_chips = dealer_object.dealer_chips_win()
  print(total_chips)
  print(dealer_chips_total)
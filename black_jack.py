import math
from collections import namedtuple
import random

values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ["Spades", "Hearts" ,"Diamonds","Clubs"]


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def draw(deck, hand, hand_sum):
    drawed_card = random.choice(deck)
    deck.remove(drawed_card)

    hand.append(drawed_card)
    hand_sum = hand_value(drawed_card,hand_sum) 
    
    return deck, hand, hand_sum

def ace_check(sum_hand):
    if (sum_hand+11)>21:
        return 1
    else: 
        return 11

def hand_value(card,sum):
    pip_value = {'2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack': 10,'Queen':10,'King':10,'Ace':ace_check(sum)}

    card_value = pip_value[card.value]

    sum += card_value

    return sum

def new_game():
    deck = [Card(value, suit) for value in values for suit in suits]
    dealer_hand = []
    player_hand = []
    dealer_sum = 0
    player_sum = 0

    deck, dealer_hand, dealer_sum = draw(deck, dealer_hand, dealer_sum)

    print("Dealer drew " + dealer_hand[0].value +  " of " + dealer_hand[0].suit)
    print("Dealersum: " + str(dealer_sum))

    deck, player_hand, player_sum = draw(deck, player_hand, player_sum)
    deck, player_hand, player_sum = draw(deck, player_hand, player_sum)

    print("Player drew " + player_hand[0].value +  " of " + player_hand[0].suit)
    print("Player drew " + player_hand[1].value +  " of " + player_hand[1].suit)
    print("Player sum: " + str(player_sum))

    
    while player_sum <21:
        x = input("Hit?")
        if x == "":
            deck, player_hand, player_sum = draw(deck, player_hand, player_sum)
            print("Player drew " + player_hand[-1].value +  " of " + player_hand[-1].suit)
            print("Player sum: " + str(player_sum))
            if player_sum>21:
                print("Bust!")
        
        else:
            break

    while dealer_sum<17:
        deck, dealer_hand, dealer_sum = draw(deck, dealer_hand, dealer_sum)
        print("Dealer drew " + dealer_hand[-1].value +  " of " + dealer_hand[-1].suit)
        print("Dealer sum: " + str(dealer_sum))
    
    if player_sum > dealer_sum:
        print("You win!")
    if player_sum < dealer_sum:
        print("You lose!")
    if player_sum == dealer_sum:
        print("Tie..")


new_game()


'''

while dealer_sum<21:
    drawed_card, deck = dealing(deck)
    

    print("Dealer drawed " + drawed_card.value +  " of " + drawed_card.suit)
    print("Sum: " + dealer_sum)

'''

'''


print(deck.copy())

'''

'''
def suit_maker(suit_color):
    suit = []

    suit{"Ace of " + suit_color)

    for i in range(2,11):
        suit[suit_color + " " + str(i)]

    suit.append("Jack of " + suit_color)
    suit.append("Queen of " + suit_color)
    suit.append("King of " + suit_color)

    return suit

spades = suit_maker("Spades")
hearts = suit_maker("Hearts")
diamonds = suit_maker("Diamonds")
clubs = suit_maker("Clubs")

deck_of_cards = spades + hearts + diamonds + clubs

print(deck_of_cards)
'''


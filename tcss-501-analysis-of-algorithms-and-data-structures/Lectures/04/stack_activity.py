#
# ---------- SETUP CODE----------
#     YOU DO NOT NEED TO EDIT
#

import random

class Stack:
    class StackNode:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        if data is None:
            return

        n = Stack.StackNode(data)

        if self.is_empty():
            self.top = n
        else:
            n.next = self.top
            self.top = n

        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            r = self.top
            self.top = self.top.next
            self.size -= 1
            return r.data

    def peek(self):
        return self.top.data if not self.is_empty() else None

    def __str__(self):
        result = ""
        current = self.top
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next
        return result


class Card:
    def __init__(self, suit, value):
        self.my_suit = suit
        self.my_value = value

    def __str__(self):
        return self.my_value + " of " + self.my_suit

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.my_suit == other.my_suit and self.my_value == other.my_value
        return False

def generate_deck():
    deck = Stack()
    for suit in ["Spades", "Clubs", "Hearts", "Diamonds"]:
        for value in ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                      "King"]:
            my_card = Card(suit, value)
            deck.push(my_card)
    return deck

#
# ---------- END SETUP CODE ----------
#     Edit things below here....
#

#
# ---------- EXAMPLE 1 ----------
# CREATING A DECK OF CARDS
#
print("\n---------- EXAMPLE 1 ----------")

deck = generate_deck()
print(deck)
print("That's a deck of cards!")

#
# ---------- EXAMPLE 2 ----------
# CREATING 2 CARDS AND RANDOMLY PICKING ONE
# You can use random.choice([list of things]) to make random choices
#
print("\n---------- EXAMPLE 2 ----------")

card1 = Card("Spades", "Ace")
card2 = Card("Spades", "Jack")
random_card = random.choice([card1, card2])

print("Randomly picked card:")
print(random_card)

#
# ---------- CHALLENGE 1 ----------
# Write the draw_cards function below, it should take the deck, and then draw
# number_of_cards from it to create a new stack. Return the new stack as the hand of cards.
# Remove the exit() statement once you start this challenge.
# This function should be O(n)
#
# print("\n---------- CHALLENGE 1 ----------")

def draw_cards(deck, number_of_cards):
    # pop the top 5 cards
    hand = Stack()
    for i in range(number_of_cards):
        card = deck.pop()
        hand.push(card)
    return hand
        

# deck = generate_deck()
# hand = draw_cards(deck, 5)

# print("Hand:")
# print(hand)

# print("Deck:")
# print(deck)

#
# ---------- CHALLENGE 2 ----------
# Complete the pull_card_from_deck function, it takes the deck object,
# and then finds a specific card in the deck (the card parameter) and removes
# that card from the deck. Return the card object that you removed.
# This function should be O(n).
#
# Discussion: Could this function ever be O(log(n))? What assumptions would need to be made?
#
# print("\n---------- CHALLENGE 2 ----------")

# def pull_card_from_deck(deck, card):
#     new_deck = Stack()
#     while not deck.is_empty():
#         top_card = deck.pop()
#         if not card.__eq__(top_card):
#             new_deck.push(top_card)
#     print(new_deck)
#     while not new_deck.is_empty():
#         top_card = new_deck.pop()
#         deck.push(top_card)

# deck = generate_deck()
# print(deck)
# pull_card_from_deck(deck, Card("Spades", "Two"))

# print("Deck:")
# print(deck)

#
# ---------- CHALLENGE 3 ----------
# Complete the deal_hands function below. This function should deal
# a number of hands (number_of_hands) from the deck and return each hand
# of cards as a list of Stacks. So create a list and add multiple stacks to the
# list. This is a good example of how you can use multiple data structures
# at the same time!
#
# print("\n---------- CHALLENGE 3 ----------")

# def deal_hands(deck, number_of_hands, cards_per_hand):
#     hands = []
#     for i in range(number_of_hands):
#         hand = []
#         for j in range(cards_per_hand):
#             card = deck.pop()
#             hand.append(card)
#         hands.append(hand)
#     return hands
            

# deck = generate_deck()
# hands = deal_hands(deck, 3, 5)

# for hand in hands:
#     print("Hand:")
#     for card in hand:
#         print(card)


#
# ---------- CHALLENGE 4 ----------
# Using your previous draw_cards function, write a function that
# takes a hand of cards and checks if the hand is a flush
# (all of the cards in the hand are the same suit)
# This should be O(n).
#
# Discussion: Could this function ever be O(1)?
#
# print("\n---------- CHALLENGE 4 ----------")

# def is_flush(hand):
#     if hand.is_empty():
#         return True
#     first_card = hand.pop()
#     suit = first_card.my_suit
#     while not hand.is_empty():
#         card = hand.pop()
#         if not card.my_suit.__eq__(suit):
#             return False
#     return True
        

# deck = generate_deck()
# hand_one = draw_cards(deck, 5)
# hand_two = draw_cards(deck, 5)
# hand_three = draw_cards(deck, 5)

# print(is_flush(hand_one))
# print(is_flush(hand_two))
# print(is_flush(hand_three))


#
# ---------- CHALLENGE 5 ----------
# Complete the function below to emulate as best as you can the
# riffle shuffle shuffling technique. So split the deck into two Stacks
# and then combine the decks back together by randomly pulling a card from the
# two stacks of cards.
# You can use random.choice(list) to randomly pick an element from a list
#
# This function should be O(n)
#
exit()
print("\n---------- CHALLENGE 5 ----------")

def riffle_shuffle(deck):
    left_deck = Stack()
    right_deck = Stack()

    # Split the Deck (Starter code hint)
    cards_per_pile = deck.size // 2
    for card in range(cards_per_pile):
        left_deck.push(deck.pop())

    for card in range(cards_per_pile):
        right_deck.push(deck.pop())


    # Random Riffle Part
    while not left_deck.is_empty() or not right_deck.is_empty():
        
        pass


deck = generate_deck()
riffle_shuffle(deck)
riffle_shuffle(deck)
riffle_shuffle(deck)

print("Deck:")
print(deck)

#
# ---------- CHALLENGE 6 ----------
# Write the function below to emulate as best as you can
# the overhand shuffle technique. So split the deck into two Stacks randomly
# and then put all of the cards from one pile on the top or bottom of the
# other stack.
# You can use random.randint(lower, upper) to generate random integers
#
# This function should be O(n)
#
exit()
print("\n---------- CHALLENGE 6 ----------")

def overhand_shuffle(deck):
    pass

deck = generate_deck()
overhand_shuffle(deck)

print("Deck:")
print(deck)

# ---------- BONUS CHALLENGES ----------
#
# If you have completed the tasks above and have extra time, try and complete these tasks:
# B1: Write a function to check if the hand is a Straight
# B2: Write a function to check if a hand of cards is a Blackjack
# B3: Write a function that does a false shuffle, do some operations on the deck
#     that ultimately end up doing nothing.
exit()
print("\n---------- BONUS CHALLENGES ----------")

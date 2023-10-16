#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:50:59 2023

@author: ndrineavdiu
"""

"""
My name is Ndrine Avdiu  (A01762207), I've been coding for the last few years, on the first year i was coding i had to code a Blackjack game, I couldn't do it is seemed too hard, I got a bad grade (5/20) and i decided to take my revenge.

That it why I decided to work on a Python project for Blackjack and it happens to be my all-time favorite card game. The thrill of the game, the strategy involved, and the possibility of hitting a perfect "21" makes it an exciting choice for a programming project.

Blackjack, also known as "21," is a classic card game played in casinos and friendly gatherings worldwide. The goal of the game is simple: to beat the dealer by having a hand value closer to 21 without going over. It's a game that combines both luck and skill, making it one of the most popular choices for casino enthusiasts.

For my Python project, I'm excited to create a digital version of Blackjack. To make it even more challenging and engaging, I've decided to add three different variations of the game: Standard Blackjack, Blackjack with a Twist, and Spanish 21. Each variant has its unique rules and gameplay elements, which will test my coding skills and create a diverse gaming experience for players.

I'll be implementing the rules, shuffling and dealing of cards, calculating hand values, and simulating the decision-making process of hitting or standing for all three types of Blackjack. As I delve into the world of programming, I look forward to the challenges and learning opportunities this project will offer. I believe that combining my passion for Blackjack with coding skills will result in a rewarding and enjoyable endeavor.
"""


import random

# Creating the card game
"""
Process: - creating ranks and suits
         - creating deck of cards
         - shuffling the cards from the deck
Output: Deck shuffled
"""
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Function to calculate hand value
"""
Input: hand (list)
process: - initialize value to 0 and num_aces to 0.
         - loop through each card in the hand
         - check the value of the ace
         - check the value of each card and add it
         -verify that it is not greater than 21, if so finish
Output: Calculated hand
"""
def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card['rank']
        if rank == 'A':
            value += 11
            num_aces += 1
        else:
            values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
            value += values.get(rank, 0)

    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value

# Function to display the hand
"""
Input: hand (list)
Process: - Get rank and suit from the card
Output: card's name
"""
def display_hand(hand):
    for card in hand:
        print(card['rank'] + ' of ' + card['suit'])


# Function for the Blackjack game
"""
Input: hit or stand
Process: - Create a deck of cards
         - Deal two cards to the player and two cards to the dealer from the deck
         - Game loop
         - Display the player's hand
         - Calculate the value of the player's hand
         - Prompt the player to choose to 'hit' or 'stand'
Output: Winner
"""
def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]


    while True:
        print("\nYour hand:")
        display_hand(player_hand)
        player_value = calculate_hand_value(player_hand)
        print("Value of your hand:", player_value)

        if player_value == 21:
            print("Blackjack! You win.")
        
            break
        elif player_value > 21:
            print("You busted. Dealer wins.")
            
            break

        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
        else:
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())

            print("\nDealer's hand:")
            display_hand(dealer_hand)
            dealer_value = calculate_hand_value(dealer_hand)
            print("Value of the dealer's hand:", dealer_value)

            if dealer_value > 21:
                print("Dealer busted. You win!")
               
            elif dealer_value >= player_value:
                print("Dealer wins.")
                
            else:
                print("You win!")
                
            break


# Calculate hand value with a twist
"""
Input: hand (list)
process: - initialize value to 0 and num_aces to 0.
         - loop through each card in the hand
         - check the value of the ace
         - check the value of each card and add it
         -verify that it is not greater than 21, if so finish
Output: Calculated hand
"""
def calculate_hand_value_blackjackTwist(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card['rank']
        if rank == 'A':
            value += 1  #In this twist, 'A' is worth 1 point
            num_aces += 1
        else:
            values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
            value += values.get(rank, 0)

    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value

# Function for the Blackjack with a twist
"""
Input: hit or stand
Process: - Create a deck of cards
         - Deal two cards to the player and two cards to the dealer from the deck
         - Game loop
         - Display the player's hand
         - Calculate the value of the player's hand
         - Prompt the player to choose to 'hit' or 'stand'
Output: Winner
"""
def play_blackjack_with_twist():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        print("\nYour hand:")
        display_hand(player_hand)
        player_value = calculate_hand_value(player_hand)
        print("\nValue of your hand:", player_value)

        if player_value == 21:
            print("\nBlackjack! You win.")
            break
        elif player_value > 21:
            print("\nYou busted. Dealer wins.")
            break

        action = input("\nDo you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
        else:
            while calculate_hand_value_blackjackTwist(dealer_hand) < 17:
                dealer_hand.append(deck.pop())

            print("\nDealer's hand:")
            display_hand(dealer_hand)
            dealer_value = calculate_hand_value_blackjackTwist(dealer_hand)
            print("\nValue of the dealer's hand:", dealer_value)

            if dealer_value > 21:
                print("\nDealer busted. You win!")
            elif dealer_value >= player_value:
                print("\nDealer wins.")
            else:
                print("\nYou win!")
            break

# Create a Spanish deck
"""
Process: - creating ranks and suits without the 10
         - creating deck of cards
         - shuffling the cards from the deck
Output: Deck shuffled
"""
def create_spanish_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Calculate hand value in Spanish 21
"""
Input: hand (list)
process: - initialize value to 0 and num_aces to 0.
         - loop through each card in the hand
         - check the value of each card and add it
         -verify that it is not greater than 21, if so finish
Output: Calculated hand
"""
def calculate_spanish_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card['rank']
        if rank == 'A':
            value += 1  # In Spanish 21, 'A' is worth 1 point
            num_aces += 1
        elif rank in ['J', 'Q', 'K']:
            value += 10  #Face cards are worth 10 points
        else:
            value += int(rank)

    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value

# Function for Spanish 21
"""
Input: hit or stand
Process: - Create a deck of cards
         - Deal two cards to the player and two cards to the dealer from the deck
         - Game loop
         - Display the player's hand
         - Calculate the value of the player's hand
         - Prompt the player to choose to 'hit' or 'stand'
Output: Winner
"""
def play_spanish_21():
    deck = create_spanish_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        print("\nYour hand:")
        display_hand(player_hand)
        player_value = calculate_spanish_hand_value(player_hand)
        print("Value of your hand:", player_value)

        if player_value == 21:
            print("\nSpanish 21! You win.")
            break
        elif player_value > 21:
            print("\nYou busted. Dealer wins.")
            break

        action = input("\nDo you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
        else:
            while calculate_spanish_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())

            print("\nDealer's hand:")
            display_hand(dealer_hand)
            dealer_value = calculate_spanish_hand_value(dealer_hand)
            print("\nValue of the dealer's hand:", dealer_value)

            if dealer_value > 21:
                print("\nDealer busted. You win!")
            elif dealer_value >= player_value:
                print("\nDealer wins.")
            else:
                print("\nYou win!")
            break
        
    
        
"""
Process: Print every line
Output: the menu
"""
def menu():
    print("\nChoose a variety of Blackjack:")
    print("\n1. Standard Blackjack")
    print("2. Blackjack with a Twist")
    print("3. Spanish 21")
    print("4. Check the rules")
    print("5. Quit")
    
# Function to choose the variety of Blackjack 
"""
Input: Choice
Process: - Choice impacts what we are doing
         - Call function 
Output: Game
"""
def main():
    while True:
        menu()
        choice = input("Enter the number of your choice: \n")
        if choice == '1':
            print("You selected Standard Blackjack.")
            play_blackjack()
        elif choice == '2':
            print("You selected Blackjack with a Twist.")
            play_blackjack_with_twist()
        elif choice == '3':
            print("You selected Spanish 21.")
            play_spanish_21()
        elif choice=="4":
            file=open("rules.txt","r")
            rules=file.read()
            print(rules)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option (1-4).")

main()


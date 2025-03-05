# Web Services and Application (WSAA)
# Assignment - Deal Cards (Week 2)
# Author: E. Qejvani

######## Task ########
# look at the the page 'Deck of Cards API'   https://deckofcardsapi.com/
# This is an API that simulates dealing a deck of cards
# Write a program that "deals" (prints out) 5 cards

import requests
import json

# Function to shuffle a new deck of cards. It returns the deck id.
def shuffle_deck():
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url)
    # Checking if the API request was successful
    if response.status_code == 200:
        print("\nConnection with the API made.\n")
        data = response.json()
        deck_id = data['deck_id']
        print(f"Deck ID: {deck_id}")  # Print out the deck ID.
        return deck_id
    else:
        raise Exception(f"Non-success status code: {response.status_code}")  #  # Error message in case of unsuccessful request.
        # (ref: https://realpython.com/python-requests/)
    

# Function to analyze the drawn cards for pairs, triples, straights, or same suit.
def analyze_hand(card_values, card_suits):
    # Dictionary initialization (See reference in README file)
    court_cards = {"ACE": 1, "KING": 13, "QUEEN": 12, "JACK": 11}
    
    numeric_values = []

    for value in card_values:
        if value:  # checking if value is empty.
            if value.isdigit():
                numeric_values.append(int(value))  # Convert number strings to integers
            else:
                numeric_values.append(court_cards.get(value, 0))  # Get value from dictionary

        numeric_values.sort()

    # Checking for pairs, triples, straights, or all same suit.
    value_counts = {value: numeric_values.count(value) for value in set(numeric_values)}
    if 3 in value_counts.values():
        print("Congratulations! You have a triple.")
    elif 2 in value_counts.values():
        print("Congratulations! You have a pair.")
    if len(set(numeric_values)) == 5 and numeric_values[-1] - numeric_values[0] == 4:
        print("Congratulations! You have a straight.")
    if len(set(card_suits)) == 1:
        print("Congratulations! All cards are of the same suit.")

# Function to draw cards from a given deck.
def deal_cards(deck_id, count=5):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    response = requests.get(url)
    # Checking if the API request was successful.
    if response.status_code == 200:
        cards = response.json().get('cards', [])
        card_values = []
        card_suits = []
        # Print each card's value and suit.
        for i, card in enumerate(cards, 1):
            card_values.append(card['value'])
            card_suits.append(card['suit'])
            print(f"Card {i}: {card['value']} of {card['suit']}")
        
        # Analyze the hand for combinations by calling analyze_hand function.
        analyze_hand(card_values, card_suits)
    else:
        raise Exception(f"Non-success status code: {response.status_code}")  # Error message in case of unsuccessful request.

# Main program:
if __name__ == "__main__":
    deck_id = shuffle_deck()  # call shuffle_deck function, return deck_id.
    if deck_id:
        print("\nDealing 5 cards:\n") 
        deal_cards(deck_id)  # call function deal_cards using deck_id returning from shuffle_deck function.

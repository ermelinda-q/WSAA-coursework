# README - WSAA ASSIGNMENTS

### Author: E. Qejvani
***

### Topic 2 - Deck of Cards.

**Task** 
Look at the the page Deck of Cards API: https://deckofcardsapi.com/. This is an API that simulates dealing a deck of cards.
Write a program that "deals" (prints out) 5 cards.First you need to shuffle the cards using: https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1
Get the deck_id. With the deck_id you can get the cards: https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2.
The above example gets two cards.
From there you need to print the value and the suit of each card. Save the file as assignment2-carddraw.py (or as a notebook).
Last few marks:
Check if the user has drawn a pair, triple, straight, or all of the same suit and congratulate the user.

**Program Structure**

```
│── import requests
│── import json
│── shuffle_deck()
│   │── API request to shuffle deck
│   │── Check response status
│   │── Parse JSON response
│   │── Extract deck_id
│   └── Return deck_id
│
│── analyze_hand(card_values, card_suits)
│   │── Initialize court_cards dictionary
│   │── Convert card values to numeric
│   │── Sort numeric values
│   │── Check for:
│   │   ├── Pair
│   │   ├── Triple
│   │   ├── Straight
│   │   └── Same suit
│
│── deal_cards(deck_id, count=5)
│   │── API request to draw cards
│   │── Check response status
│   │── Extract card values and suits
│   │── Print drawn cards
│   └── Call analyze_hand()
│
└── __main__
    │── Call shuffle_deck()
    │── If deck_id exists:
    │   ├── Print message
    │   └── Call deal_cards(deck_id)
```

**References**
- [Deck of Cards API](https://deckofcardsapi.com)
- [List of Api Status Code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [Python Requests](https://realpython.com/python-requests/)
- [Dictionary Initialization with common dictionary](https://www.geeksforgeeks.org/python-dictionary-initialization-with-common-dictionary)

***

### Topic 4 - Assignment 03

**Task**

Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".

- Upload this program to the same repository used for the first assignment.
- Save this assignment as "assignment03-cso.py"
- This program should not be a long one
- No need to reformat or analyze the data in any way.
- It should be about 10ish lines long.
- Find the dataset in CSO.ie, try economic and then finance, then finance indicators.

**Program Structure**

```
Importing Modules
├── import requests  # Handles HTTP requests
├── import json      # Handles JSON data processing

API Configuration
├── base_url         # Base API endpoint
│   ├── "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
│
├── format_details   # Specifies response format
│   ├── "/JSON-stat/2.0/en"
│
├── dataset_id       # Dataset identifier for API request
│   ├── "FIQ02"

Function: get_all_as_file(dataset)
├── Opens "cso.json" in write mode
├── Calls get_all_data(dataset) to fetch data
├── Saves retrieved data to "cso.json"

Function: get_all_data(dataset)
├── Constructs full API request URL
├── Sends GET request to API
├── Returns JSON response

Main Execution Block
└── if __name__ == "__main__":  
    ├── Calls get_all_as_file(dataset_id) to retrieve and save data
```

**References**

- Based on topic 4, 'Reading API's in the Wild' - WSAA lecture by A. Beatty.
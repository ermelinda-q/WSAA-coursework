# ASSIGNMENTS

## Web Services And Applications - WSAA

#### by E. Qejvani
***
This README has been written with [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.
You should refer to that documentation for more information on writing an appropriate README for visitors to your repository.
You can find out more about [writing in MarkDown in GitHub's documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

***
## About this Repository

This git sub-repository (WSAA/assignments) holds all the assignment files of Web Services and Applications module, as part of my [Hdip in Computer Science in Data Analytics](https://www.atu.ie/courses/higher-diploma-in-science-data-analytics#:~:text=You%20are%20a%20Level%208,topics%20in%20your%20original%20degree) in [ATU](https://www.atu.ie/).

**Structure of this Sub-Repository**

```
├── assignments/                    # Main subfolder of the assignments
├──── data/                         # Folder containing/saving data files used by the scripts.
│       ├── cso.json                # JSON file used in assignment03-cso.py
│       ├── original-text.txt       # Original reference text - assignment 4
│       └── text_to_change.txt      # Text to be modified - assignment 4
├──── assignment2-carddraw.py       # Assignment 2 - python file
├──── assignment03-cso.py           # Assignment 3 - python file
├──── assignment04-github.py        # Assignment 4 - python file
├──── config.py (hidden)            # Stores the GitHub API key (not included in repo)
└──── README.md                     # Project overview and instructions (this file)
```
***
## About the Assignments

The module comprises three assignments, each described in detail below.

***
### Assignment 1: Topic 2 - Deck of Cards.

_Filename:_ assignment2-carddraw.py

**Task** 
Look at the the page Deck of Cards API: https://deckofcardsapi.com/. This is an API that simulates dealing a deck of cards.
Write a program that "deals" (prints out) 5 cards.First you need to shuffle the cards using: https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1
Get the deck_id. With the deck_id you can get the cards: https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2.
The above example gets two cards.
From there you need to print the value and the suit of each card. Save the file as assignment2-carddraw.py (or as a notebook).
Last few marks:
Check if the user has drawn a pair, triple, straight, or all of the same suit and congratulate the user.

**File Structure**

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

### Assignment 2: Topic 4 - Reading API's in the Wild

_Filename:_ assignment03-cso.py

**Task**

Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".

- Upload this program to the same repository used for the first assignment.
- Save this assignment as "assignment03-cso.py"
- This program should not be a long one
- No need to reformat or analyze the data in any way.
- It should be about 10ish lines long.
- Find the dataset in CSO.ie, try economic and then finance, then finance indicators.

**File Structure**

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

***

### Assignment 3: Topic 5 - Authentication

_Filename:_ assignment04-github.py

**Task**

Write a program in python that will read a file from a GitHub repository.
The program should:
    - Replace all the instances of the text "Andrew" with your name.
    - Commit those changes and push the file back to the repository.

**File Structure**

```
Importing Modules
├── from github import Github   # GitHub API wrapper
├── from config import config   # Import API key from config.py (The file is not uploaded in GitHub)

Authentication and Setup
├── apikey                      # GitHub key from config (in config.py file)
├── REPO_NAME                   # Target repository
├── FILE_PATH                   # Path to the file to modify in the repo
├── g = Github(apikey)          # Authenticated GitHub client
├── repo = g.get_repo(...)      # Target repository object

File Retrieval and Modification
├── file = repo.get_contents(...)         # Fetch file metadata and content
├── file_content = file.decoded_content   # Decode file content to text
├── updated_content = file_content.replace(...)  # Replace target text
├── Append modification notice if not already present

Conditional Update
├── if updated_content != file_content:
│   ├── repo.update_file(...)             # Commit updated content to GitHub
│   └── print("File updated and changes pushed successfully.")
└── else:
    └── print("No changes needed.")
```

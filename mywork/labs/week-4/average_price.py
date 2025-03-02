# Web Services and Applications - WSAA
# Topic 4 labs
# Author: E. Q.

# This program reads an api file and works out the average book price from all the books on the server.

import requests

# Server URL
url = "http://andrewbeatty1.pythonanywhere.com/books"  

# This function reads all books from the server.
def read_books():
    response = requests.get(url)
    return response.json()

# function to calculate average price.
def average_price(books):
    total_books = [book['price'] for book in books if 'price' in book]
    return sum(total_books) / len(total_books)

if __name__ == "__main__":
    books = read_books()
    avg_price = average_price(books)
    print(f"The average book price is: {avg_price:.2f}")

import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

# google_url = "http://google.com"
# google_response = requests.get(google_url)

# print(google_response.text)    # google page in html. works!

# response = requests.get(url)
# print(response.json())

# this functions returns all books
def readbooks():
    response = requests.get(url)
    return response.json()

# reading a book by id
def readbook(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()


# write the code to create a book
def createbook(book):
    response = requests.post(url, json=book)
    
    return response.json()

# write and update function
def updatebook(id, book):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

# delete book function by id
def deletebook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

# main program
if __name__ == "__main__":
    book = {
        "Author": "just me",
        "Title": "another test",
        "Price": 222
    }
    # print(readbooks())
    # print(readbook(1597))
    print(createbook(book))
    
    
    


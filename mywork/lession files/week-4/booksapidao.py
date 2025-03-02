import requests
import json

url = "http://andrewbeatty1.pythonanywhere.com/books"

# functions to use in this lesson:

def getallbooks():
    response = requests.get(url)
    return response.json()

def getbook_by_id(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()


# create book
def create_book(book):
    pass

def update_book(book_diff):
    pass
def delete_book(id):
    get_url = url + "/" + str(id)
    response =  requests.delete(get_url)
    return response.json()


if __name__ == "__main__":
    # print(getallbooks())
    print(getbook_by_id(300))
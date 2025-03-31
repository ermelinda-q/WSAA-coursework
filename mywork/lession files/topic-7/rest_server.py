# A simple flask server
# implementing most of the basic functions

from flask import Flask, request, jsonify, abort
from bookDAO_skeleton import book_dao


app = Flask(__name__)

# index file of the server.
@app.route("/")
def index():
    return "Working with a flask server"

# Get all.
@app.route("/books", methods=["GET"])
def getall():
    return jsonify(book_dao.get_all())

# Find by id.
@app.route("/books/<int:id>", methods=["GET"])
def findbyid(id):
    return jsonify(book_dao.find_by_id(id))

# Create
@app.route("/books", methods=["POST"])
def create():
    # read json from the body
    jsonstring = request.json
    book = {}
    
    if "title" not in jsonstring:
        abort(403)    
    book["title"] = jsonstring["title"]
    if "author" not in jsonstring:
        abort(403)
    book["author"] = jsonstring["author"]
    if "price" not in jsonstring:
        abort(403)
    book["price"] = jsonstring["price"]
    return jsonify(book_dao.create(book))

# Update.
@app.route("/books/<int:id>", methods=["PUT"])
def update(id):
    # read json from the body
    jsonstring = request.json
    book = {}
    
    if "title" in jsonstring:  
        book["title"] = jsonstring["title"]
    if "author" in jsonstring:
        book["author"] = jsonstring["author"]
    if "price" in jsonstring:   
        book["price"] = jsonstring["price"]
    return jsonify(book_dao.update(id, book))
 
# Delete
@app.route("/books/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify(book_dao.delete(id))   

if __name__== "__main__":
    app.run(debug=True)


# A simple flask server
# implementing most of the basic functions

from flask import Flask, request

app = Flask(__name__)

# index file of the server.
@app.route("/")
def index():
    return "Working with a flask server"

# Get all.
@app.route("/books", methods=["GET"])
def getall():
    return "Get all"

# Find by id.
@app.route("/books/<int:id>", methods=["GET"])
def findbyid(id):
    return f"Find by id {id}"

# Create
@app.route("/books", methods=["POST"])
def create():
    # read json from the body
    jsonstring = request.json
    return f"Create {jsonstring}"

# Update.
@app.route("/books/<int:id>", methods=["PUT"])
def update(id):
    jsonstring2 = request.json
    return f"update {id} {jsonstring2}"

# Delete
@app.route("/books/<int:id>", methods=["DELETE"])
def delete(id):
    return f"delete {id}"    

if __name__== "__main__":
    app.run(debug=True)


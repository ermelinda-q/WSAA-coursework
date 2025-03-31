# Lab 06.01 - WSAA
# Author: E.Q.
# Based on the lecturers of topic 6.


from flask import Flask, request, redirect, abort

app = Flask(__name__, static_url_path="", static_folder="staticpages")

@app.route("/")
def index():
    return "Hello. This is lab 06"

# get all
@app.route("/books", methods=["GET"])
def getall():
    return "Get All"

# Get by id.
@app.route("/books/<int:id>", methods=["GET"])
def findbyid(id):
    return f"find by id {id}"

# Create
@app.route("/books", methods=["POST"])
def create():
    # read json string from the body
    jsonstring = request.json
    return f"Create {jsonstring}"

# Update
@app.route("/books/<int:id>", methods=["PUT"])
def update(id):
    jsonstring = request.json
    return f"Update {id} {jsonstring}"

# Delete
@app.route("/books/<int:id>", methods=["DELETE"])
def delete(id):
    return f"Delete {id}"


if __name__=="__main__":
    app.run(debug=True)


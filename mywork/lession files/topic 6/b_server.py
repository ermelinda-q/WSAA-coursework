# topic 6 lesson - different ways of mapping


from flask import Flask, url_for, redirect

app = Flask(__name__, static_url_path="", static_folder="staticpages")

# mapping
@app.route("/")
def index():
    return "<h1>hi there again</h1>"

# dealing with users
@app.route('/users', methods=['GET'])
def get_users():
    return "getting all users"

@app.route("/users/<username>", methods=["GET"])
def get_user_byname(username):
    return f"Hello {username}"

@app.route("/users/<int:id>", methods=["GET"])
def get_user_byid(id):
    return f"Your id is {id}"

@app.route("/users", methods=["POST"])
def create_user():
    return "creating a user"

@app.route("/users", methods=["PUT"])
def update_user():
    return "update a user"

# if there is an invalid url
@app.route("/invalid", methods=["GET"])
def testing_redirect():
    return redirect(url_for("index"))

@app.route("/square/<int:id>", methods=["GET"])
def square(id):
    return f"The square of {id} is {id**2}"

if __name__ == "__main__":
    app.run(debug=True)
    


from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "hello server C"

# taking data as arguments
@app.route("/inquery")
def inquery():
    name = request.args["name"]
    return request.args

@app.route("/inbody", methods=["POST"])
def inbody():
    name = request.json["name"]
    age = request.json["age"]
    print(request.json)
    return f"you are {name} and aged {age}"

# writing a function that will get a user:
@app.route("/user")

def get_user():
    user={
        "name": "Ermelinda",
        "age": 21
    }
    return jsonify(user)


if __name__ == "__main__":
    app.run(debug=True)
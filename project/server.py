# Flask Server file
# Author: E. Qejvani
# Based on lectures by A. Beatty

from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from fluteDAO import fluteDAO

# Set static_folder to "static"
app = Flask(__name__, static_url_path='', static_folder='static')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return app.send_static_file('index.html')


# curl "http://127.0.0.1:5000/flutes"
@app.route('/flutes')
@cross_origin()
def getAll():
    results = fluteDAO.getAll()
    return jsonify(results)


# curl "http://127.0.0.1:5000/flutes/1"
@app.route('/flutes/<int:id>')
@cross_origin()
def findById(id):
    found = fluteDAO.findByID(id)
    return jsonify(found)


# curl -i -H "Content-Type:application/json" -X POST -d "{\"fluteMaker\":\"Yamaha\",\"fluteModel\":\"YFL-222\",\"fluteLevel\":\"Beginner\",\"fluteHead\":\"Nickel\",\"fluteBody\":\"Silver\",\"fluteMechanism\":\"Closed\",\"priceRange\":1000}" http://127.0.0.1:5000/flutes
@app.route('/flutes', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400)
    flute = {
        "fluteMaker": request.json['fluteMaker'],
        "fluteModel": request.json['fluteModel'],
        "fluteLevel": request.json['fluteLevel'],
        "fluteHead": request.json['fluteHead'],
        "fluteBody": request.json['fluteBody'],
        "fluteMechanism": request.json['fluteMechanism'],
        "priceRange": request.json['priceRange'],
    }
    added = fluteDAO.create(flute)
    return jsonify(added)


# curl -i -H "Content-Type:application/json" -X PUT -d "{\"fluteMaker\":\"Yamaha\",\"fluteModel\":\"YFL-221\",\"fluteLevel\":\"Intermediate\",\"fluteHead\":\"Silver\",\"fluteBody\":\"Silver\",\"fluteMechanism\":\"Open\",\"priceRange\":1500}" http://127.0.0.1:5000/flutes/1
@app.route('/flutes/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    found = fluteDAO.findByID(id)
    if not found:
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json

    for field in ['fluteMaker', 'fluteModel', 'fluteLevel', 'fluteHead', 'fluteBody', 'fluteMechanism', 'priceRange']:
        if field in reqJson:
            found[field] = reqJson[field]

    fluteDAO.update(id, found)
    return jsonify(found)


# curl -X DELETE http://127.0.0.1:5000/flutes/1
@app.route('/flutes/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    fluteDAO.delete(id)
    return jsonify({"done": True})


if __name__ == '__main__':
    app.run(debug=True)

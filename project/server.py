# Flask Server file
# Author: E. Qejvani
# Based on lectures by A. Beatty
# Use of render_template from: https://www.geeksforgeeks.org/flask-rendering-templates/ 
# and
# https://flask.palletsprojects.com/en/stable/quickstart/

from flask import Flask, jsonify, request, abort, render_template
from flask_cors import CORS, cross_origin
from fluteDAO import fluteDAO

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/view_all')
@cross_origin()
def view_all():
    return render_template('view_all.html')

@app.route('/find_flute')
@cross_origin()
def find_flute():
    return render_template('find_flute.html')

@app.route('/create_flute')
@cross_origin()
def create_flute_page():
    return render_template('create_flute.html')

@app.route('/update_flute')
@cross_origin()
def update_flute_page():
    return render_template('update_flute.html')

@app.route('/delete_flute')
@cross_origin()
def delete_flute_page():
    return render_template('delete_flute.html')


# ---------- API ROUTES ----------

# Get all flutes
@app.route('/flutes', methods=["GET"])
@cross_origin()
def getAll():
    results = fluteDAO.getAll()
    return jsonify(results)


# Find flute by ID
@app.route('/flutes/<int:id>', methods=["GET"])
@cross_origin()
def findById(id):
    found = fluteDAO.findByID(id)
    if not found or found == {}:
        return jsonify({"error": "Flute not found"}), 404
    return jsonify(found)


# Create a new flute
@app.route('/flutes', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400, description="Request body must be JSON.")

    try:
        flute = {
            "fluteMaker": request.json['fluteMaker'],
            "fluteModel": request.json['fluteModel'],
            "fluteLevel": request.json['fluteLevel'],
            "fluteHead": request.json['fluteHead'],
            "fluteBody": request.json['fluteBody'],
            "fluteMechanism": request.json['fluteMechanism'],
            "flutePrice": request.json['flutePrice'],
        }
    except KeyError as e:
        abort(400, description=f"Missing required field: {str(e)}")

    added = fluteDAO.create(flute)
    return jsonify(added), 201


# Update an existing flute
@app.route('/flutes/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    found = fluteDAO.findByID(id)
    if not found:
        return jsonify({"error": "Flute not found"}), 404

    if not request.json:
        abort(400, description="Request body must be JSON.")

    reqJson = request.json

    # Update fields if they exist in request
    for field in ['fluteMaker', 'fluteModel', 'fluteLevel', 'fluteHead', 'fluteBody', 'fluteMechanism', 'flutePrice']:
        if field in reqJson:
            found[field] = reqJson[field]

    fluteDAO.update(id, found)
    return jsonify(found)


# Delete a flute
@app.route('/flutes/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    found = fluteDAO.findByID(id)
    if not found:
        return jsonify({"error": "Flute not found"}), 404

    fluteDAO.delete(id)
    return jsonify({"done": True})


# ---------- Run the server ----------
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('itemData.json') as f:
    item_data = json.load(f)

@app.route('/', methods=['GET'])
def get_icon():
    item_id = request.args.get('id', type=int)
    if item_id is None:
        return jsonify({"error": "Missing 'id' parameter"}), 400

    for item in item_data:
        if item.get("Id") == item_id:
            return jsonify({"Id": item_id, "Icon": item.get("Icon")})

    return jsonify({"error": f"No item found with Id {item_id}"}), 404

def handler(request, response):
    return app(request.environ, response.start_response)

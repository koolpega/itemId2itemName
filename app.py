from flask import Flask, request, jsonify
import json
import os

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
            icon_name = item.get("Icon")
            image_url = f"https://ff.deaddos.online/api/images?iconName={icon_name}&key=FREE"
            return jsonify({
                "Id": item_id,
                "Icon": icon_name,
                "Image": image_url
            })

    return jsonify({"error": f"No item found with Id {item_id}"}), 404

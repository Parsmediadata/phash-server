import os
import imagehash
from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/phash', methods=['POST'])
def hash_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    try:
        file = request.files['image']
        img = Image.open(io.BytesIO(file.read()))
        hash_value = str(imagehash.phash(img))  # محاسبه pHash
        return jsonify({"phash": hash_value})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # دریافت مقدار PORT از محیط، در غیر این صورت 10000
    app.run(host='0.0.0.0', port=port)


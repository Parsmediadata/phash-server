import imagehash
from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/hash', methods=['POST'])
def hash_image():
    file = request.files['image']
    img = Image.open(io.BytesIO(file.read()))
    hash_value = str(imagehash.phash(img))
    return jsonify({"hash": hash_value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

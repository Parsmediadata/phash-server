import os
import imagehash
import base64
from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/phash', methods=['POST'])
def hash_image():
    try:
        # بررسی اینکه آیا `Base64` در درخواست وجود دارد
        data = request.json
        if 'image_base64' not in data:
            return jsonify({"error": "No Base64 image provided"}), 400

        # دریافت و تبدیل `Base64` به تصویر
        image_data = base64.b64decode(data['image_base64'])
        img = Image.open(io.BytesIO(image_data))

        # محاسبه `pHash`
        hash_value = str(imagehash.phash(img))

        return jsonify({"phash": hash_value})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # دریافت مقدار PORT از محیط
    app.run(host='0.0.0.0', port=port)



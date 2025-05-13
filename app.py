from flask import Flask, request, jsonify
from utils import save_base64_image, get_face_id
import os

app = Flask(__name__)

@app.route('/face-process', methods=['POST'])
def process_image():
    try:
        data = request.json
        base64_image = data.get("image_base64")

        if not base64_image:
            return jsonify({"error": "Missing image_base64"}), 400

        image_path = save_base64_image(base64_image)
        face_id = get_face_id(image_path)

        os.remove(image_path)

        if face_id is None:
            return jsonify({"error": "No face detected"}), 422

        return jsonify({"face_id": face_id}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

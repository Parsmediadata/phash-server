import base64
import uuid
import os
from face_recognition import load_image_file, face_encodings

TEMP_DIR = "temp_images"
os.makedirs(TEMP_DIR, exist_ok=True)

def save_base64_image(base64_str):
    image_data = base64.b64decode(base64_str)
    filename = f"{uuid.uuid4().hex}.jpg"
    filepath = os.path.join(TEMP_DIR, filename)
    
    with open(filepath, "wb") as f:
        f.write(image_data)
    
    return filepath

def get_face_id(image_path):
    image = load_image_file(image_path)
    encodings = face_encodings(image)
    
    if not encodings:
        return None
    
    # تبدیل بردار چهره به یک شناسه هش‌شده
    face_id = hash(tuple(encodings[0]))
    return str(face_id)

from fastapi import FastAPI, UploadFile, File
import face_recognition
import io
from PIL import Image

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Face encoding API is running"}

@app.post("/encode_face/")
async def encode_face(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = face_recognition.load_image_file(io.BytesIO(image_bytes))
    encodings = face_recognition.face_encodings(image)

    if not encodings:
        return {"error": "No face found"}

    return {"encoding": encodings[0].tolist()}

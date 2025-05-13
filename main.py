from fastapi import FastAPI, UploadFile, File
import face_recognition
import io

app = FastAPI()

@app.get("/")
def root():
    return {"status": "سرور فعال است"}

@app.post("/encode_face/")
async def encode_face(file: UploadFile = File(...)):
    # خواندن تصویر
    image_bytes = await file.read()
    image_stream = io.BytesIO(image_bytes)

    # پردازش چهره
    image = face_recognition.load_image_file(image_stream)
    encodings = face_recognition.face_encodings(image)

    if not encodings:
        return {"error": "هیچ چهره‌ای یافت نشد"}

    return {"encoding": encodings[0].tolist()}

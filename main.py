from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import io
import face_recognition

app = FastAPI()

@app.post("/get_face_code")
async def get_face_code(file: UploadFile = File(...)):
    # خواندن داده‌های فایل تصویر
    image_bytes = await file.read()

    # تبدیل تصویر بایت‌ها به شی تصویر و استخراج ویژگی‌های چهره
    image = face_recognition.load_image_file(io.BytesIO(image_bytes))

    # استخراج ویژگی‌های چهره
    face_encodings = face_recognition.face_encodings(image)

    # بررسی اینکه چهره‌ای شناسایی شده است یا نه
    if len(face_encodings) > 0:
        face_code = face_encodings[0].tolist()  # تبدیل آرایه به لیست برای ارسال به JSON
    else:
        face_code = None

    return {"face_code": face_code}

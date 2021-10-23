from typing import Optional
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, Form
import aiofiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [""]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    async with aiofiles.open(file.filename, 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write
    return {"filename": file.filename}

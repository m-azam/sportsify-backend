import os
from typing import Optional
import cv2
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, Form
import aiofiles
from fastapi.middleware.cors import CORSMiddleware
from services.object_detect import *
from modules.gif_generator.generate import *
import base64
from PIL import Image
from PIL.ExifTags import TAGS


app = FastAPI()

origins = [""]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)

def create_frames(filename):
    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()
    count = 0
    while count < 1:
        
        cv2.imwrite("services/frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1


def findImage(filename):
    create_frames(filename)
    return detect_object()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    async with aiofiles.open(file.filename, 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)# async write
        centered_object = findImage(file.filename)
        
        
    return {"centered_object": centered_object.title()}




from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from test import getVideoStreaming, getVideoStreaming1, getVideoStreaming2, getVideoStreaming3, getVideoStreaming4, \
    getVideoStreaming5

app = FastAPI()

origins = ["*"]

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"Hello": "LiVE ~!!"}

def video_streaming_response(generator_func):
    return StreamingResponse(generator_func(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/fire")
def fire_video():
    return video_streaming_response(getVideoStreaming)

@app.get("/video1")
def video_1():
    return video_streaming_response(getVideoStreaming1)

@app.get("/video2")
def video_2():
    return video_streaming_response(getVideoStreaming2)

@app.get("/video3")
def video_3():
    return video_streaming_response(getVideoStreaming3)

@app.get("/video4")
def video_4():
    return video_streaming_response(getVideoStreaming4)

@app.get("/video5")
def video_5():
    return video_streaming_response(getVideoStreaming5)
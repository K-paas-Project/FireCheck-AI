from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from test import getVideoStreaming, getVideoStreaming1, getVideoStreaming2, getVideoStreaming3, getVideoStreaming4, \
    getVideoStreaming5

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "LiVE ~!!"}

@app.get("/fire")
def video():
    return StreamingResponse(getVideoStreaming(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/video1")
def video():
    return StreamingResponse(getVideoStreaming1(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/video2")
def video():
    return StreamingResponse(getVideoStreaming2(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/video3")
def video():
    return StreamingResponse(getVideoStreaming3(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/video4")
def video():
    return StreamingResponse(getVideoStreaming4(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/video5")
def video():
    return StreamingResponse(getVideoStreaming5(), media_type="multipart/x-mixed-replace; boundary=frame")

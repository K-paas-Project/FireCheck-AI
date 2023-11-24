from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from test import getVideoStreaming

app = FastAPI()

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from test import getVideoStreaming

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "PNP"}

@app.get("/video")
def video():
    return StreamingResponse(getVideoStreaming(), media_type="multipart/x-mixed-replace; boundary=frame")

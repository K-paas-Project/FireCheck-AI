FROM python:3.10

WORKDIR /app

COPY runs/detect/train35/weights/best.pt /app/runs/detect/train35/weights/best.pt
COPY as.mp4 /app/
COPY video.py /app/
COPY test.py /app/

COPY deploy.txt /app/

RUN pip install --no-cache-dir -r deploy.txt

CMD ["uvicorn", "app:video", "--host", "0.0.0.0", "--port", "8000"]
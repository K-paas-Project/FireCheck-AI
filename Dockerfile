FROM python:3.10

# Install libgl1-mesa-glx
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Set the working directory in the container
WORKDIR /app

# Copy necessary files to the /app directory in the container
COPY runs/detect/train35/weights/best.pt .
COPY as.mp4 .
COPY n1.mp4 .
COPY n2.mp4 .
COPY n3.mp4 .
COPY n4.mp4 .
COPY n5.mp4 .

# Copy Python scripts to the /app directory
COPY test.py .
COPY video.py .

# Copy requirements file and install dependencies
COPY deploy.txt .
RUN pip install --no-cache-dir -r deploy.txt

# Set the command to run when the container starts
CMD ["uvicorn", "video:app", "--host", "0.0.0.0", "--port", "8000"]

import cv2
from ultralytics import YOLO
import numpy as np
from io import BytesIO
from PIL import Image

def compress_image(image, quality=10):
    # OpenCV 이미지를 Pillow 이미지로 변환
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # 이미지를 BytesIO에 저장하고 JPEG 형식으로 압축
    output_buffer = BytesIO()
    pil_image.save(output_buffer, format="JPEG", quality=quality)

    # 압축된 이미지 바이너리를 반환
    return output_buffer.getvalue()


def getVideoStreaming():
    # Load the YOLOv8 model
    # model = YOLO('C:/Users/USER/Downloads/ultralytics-main/runs/detect/train35/weights/best.pt')
    model = YOLO('/app/best.pt')

    # 동영상 파일 사용시
    video_path = "/app/as.mp4"

    # 비디오 캡처 객체 생성
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        # YOLOv8 모델을 사용하여 프레임에 추론 수행
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # 결과가 발생하면 'event' 출력
        # if results[0].speed:
        #     print('event')
        #     yield "event: alarm\ndata: {}\n\n"

        # 이미지를 바이너리로 인코딩
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = bytearray(buffer.tobytes())

        # 이미지를 압축
        compressed_frame = compress_image(annotated_frame)

        # 바이너리 이미지를 전송
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + compressed_frame + b'\r\n')


def getVideoStreaming1():
    video_path1 = "/app/n1.mp4"
    cap = cv2.VideoCapture(video_path1)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Encode the image into binary
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
        )


def getVideoStreaming2():
    video_path1 = "/app/n2.mp4"

    cap = cv2.VideoCapture(video_path1)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Encode the image into binary
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
        )

def getVideoStreaming3():
    video_path1 = "/app/n3.mp4"

    cap = cv2.VideoCapture(video_path1)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Encode the image into binary
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
        )

def getVideoStreaming4():
    video_path1 = "/app/n4.mp4"

    cap = cv2.VideoCapture(video_path1)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Encode the image into binary
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
        )

def getVideoStreaming5():
    video_path1 = "/app/n5.mp4"

    cap = cv2.VideoCapture(video_path1)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Encode the image into binary
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
        )
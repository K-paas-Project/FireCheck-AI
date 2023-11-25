# from ultralytics import YOLO
#
# # Load Trained Model
# model = YOLO("C:/Users/USER/Downloads/ultralytics-main/runs/detect/train7/weights/best.pt")
#
# # Get Result
# results = model.predict("C:/Users/USER/Downloads/a.mp4", conf=0.4, iou=0.65, max_det=300, save=True)
#
# # Check
# for result in results:
#     labels = result.boxes.cls
# scores = result.boxes.conf
# bboxes = result.boxes.xyxy
#
# print(labels, scores, bboxes)


import cv2
from ultralytics import YOLO


def getVideoStreaming():
    # Load the YOLOv8 model
    #model = YOLO('C:/Users/USER/Downloads/ultralytics-main/runs/detect/train35/weights/best.pt')
    model = YOLO('/app/runs/detect/train35/weights/best.pt')

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
        if results[0].speed:
            print('event')
            yield "event: alarm\ndata: {}\n\n"

        # 이미지를 바이너리로 인코딩
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = bytearray(buffer.tobytes())

        # 바이너리 이미지를 전송
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')



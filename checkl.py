# from ultralytics import YOLO
#
# # Instantiate YOLO model with pre-trained weights
# model = YOLO("yolov8n.pt")
# # model.to('cuda')
#
# # Train the YOLO model on a dataset using GPU
# model.train(data="C:\\Users\\USER\\Downloads\\data\\data.yaml", epochs=20, imgsz=640, amp=False)

# import torch
#
# var = torch.__version__
# print(var)
#
#


from ultralytics import YOLO
from multiprocessing import freeze_support
import torch

def main():
    # Set the CUDA device
    torch.cuda.set_device(0)  # 0은 사용할 GPU의 번호입니다.

    # Instantiate YOLO model with pre-trained weights
    model = YOLO("yolov8n.pt")

    # Train the YOLO model on a dataset using GPU
    model.train(data="C:\\Users\\USER\\Downloads\\asd\\data.yaml", epochs=35, imgsz=640, device='cuda')

if __name__ == '__main__':
    freeze_support()
    main()

    # # Instantiate YOLO model with pre-trained weights
    # model = YOLO("yolov8n.pt")
    #
    # # Train the YOLO model on a dataset using GPU
    # model.train(data="C:\\Users\\USER\\Downloads\\data\\data.yaml", epochs=20, imgsz=640, device='cuda', amp=False, workers=0)

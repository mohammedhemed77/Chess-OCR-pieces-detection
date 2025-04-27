from multiprocessing.pool import worker

import torch

print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Device name:", torch.cuda.get_device_name(0))

# update nvidia GTX 1060 driver from
# https://www.nvidia.com/Download/index.aspx
# Update to a driver that supports CUDA 12.6:
# Go to the NVIDIA Driver Download page
# Choose:
# Product Series: GeForce 10 Series
# Product: GeForce GTX 1060
# OS: Your current Windows version
# Download and install the latest Game Ready or Studio driver
# Then restart your PC.

# print the status :
# ---------------------
# print(torch.__version__)
# print(torch.version.cuda)
# print(torch.backends.cudnn.version())
# print(torch.cuda.is_available())

# output :
# ----------
# CUDA available: True
# Device name: NVIDIA GeForce GTX 1060 with Max-Q Design
# 2.6.0+cu126
# 12.6
# 90501
# True

# train.py

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ['YOLO_SKIP_CORRUPT'] = '1'

from ultralytics import YOLO

def main():
    # Load a model
    model = YOLO("yolo11n.pt")  # Replace with your preferred model

    # UPDATE THIS PATH: local path to your dataset YAML
    data_yaml_path = "C:/Users/moham/OneDrive/Desktop/data.yaml"

    # Check if the file exists
    if not os.path.exists(data_yaml_path):
        raise FileNotFoundError(f"YAML configuration file not found: {data_yaml_path}")

    # Train the model (device=0 uses GPU, -1 uses CPU)
    results = model.train(
        data=data_yaml_path,
        epochs=20,
        imgsz=320,
        batch=32,
        workers = 0,
        device=0  # set to -1 if you're using CPU only
    )

if __name__ == '__main__':
    main()

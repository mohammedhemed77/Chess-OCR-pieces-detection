# from ultralytics import YOLO
#
# def run_detection():
#     # Load the trained YOLO model
#     model = YOLO("runs/detect/train19/weights/best.pt")  # Update path if needed
#
#     # Predict on images in the extracted_images folder
#     results = model.predict(
#         source="extracted_images",  # Folder containing images
#         save=True,                  # Save annotated images
#         conf=0.5                    # Confidence threshold
#     )
#
#     print("Detection completed. Results saved in: runs/detect/predict/")
#
# if __name__ == "__main__":
#     run_detection()
#

from ultralytics import YOLO
import os

def run_detection():
    # Load the trained YOLO model
    model = YOLO("runs/detect/train/weights/best.pt")

    # Run prediction
    results = model.predict(
        source="extracted_images",  # Folder containing images
        save=True,                  # Save annotated images
        conf=0.9                   # Confidence threshold
    )

    output_dir = "detection_outputs"
    os.makedirs(output_dir, exist_ok=True)

    for i, result in enumerate(results):
        img_path = result.path
        base_name = os.path.basename(img_path)
        file_name = os.path.splitext(base_name)[0]
        output_path = os.path.join(output_dir, f"{file_name}.txt")

        with open(output_path, "w") as f:
            boxes = result.boxes  # Get Boxes object
            for box in boxes:
                cls = int(box.cls.item())
                conf = float(box.conf.item())
                x1, y1, x2, y2 = box.xyxy[0].tolist()  # Bounding box coordinates

                f.write(f"{cls} {conf:.4f} {x1:.2f} {y1:.2f} {x2:.2f} {y2:.2f}\n")

    print(f"Detection completed. Results written to: {output_dir}")

if __name__ == "__main__":
    run_detection()

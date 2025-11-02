import cv2
import argparse
import torch
import os
from ultralytics import YOLO
import torch.serialization
import torch.nn.modules.container as container
import ultralytics.nn.tasks as tasks

# -------------------------------
# SAFE LOADING FIX (for PyTorch 2.6+)
# -------------------------------
torch.serialization.add_safe_globals([
    tasks.DetectionModel,
    container.Sequential,
])


# -------------------------------
# LOAD SOURCE FUNCTION
# -------------------------------
def load_source(source):
    """Load input source: webcam, image, or video."""
    if source == "0":
        return True, cv2.VideoCapture(0)
    img_formats = ['jpg', 'jpeg', 'png', 'tif', 'tiff', 'dng', 'webp', 'mpo']
    if source.split('.')[-1].lower() in img_formats:
        return False, cv2.imread(source)
    return True, cv2.VideoCapture(source)


# -------------------------------
# DRAW BOXES FUNCTION
# -------------------------------
def draw_boxes(image, results, names, thickness=2):
    """Draw YOLO detection boxes and labels on the frame."""
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            label = f"{names[cls_id]} {conf:.2f}"
            color = (0, 255, 0)
            cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
            cv2.putText(image, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)
    return image


# -------------------------------
# MAIN EXECUTION
# -------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=str, default="0", help="Path to video/image or '0' for webcam")
    parser.add_argument("--model", type=str, default="yolov8n.pt", help="YOLOv8 model file")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold")
    parser.add_argument("--thickness", type=int, default=2, help="Bounding box thickness")
    parser.add_argument("--save", action="store_true", help="Save detection results to disk")
    parser.add_argument("--save_dir", type=str, default="detections", help="Directory to save results")
    args = parser.parse_args()

    # Check GPU
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")

    # Auto-download model if missing
    if not os.path.exists(args.model):
        print(f"⚠️ Model file '{args.model}' not found. Downloading from Ultralytics hub...")
        YOLO(args.model)

    # Load YOLO model safely
    model = YOLO(args.model)
    model.to(device)

    # Load source
    is_video, src = load_source(args.source)

    # Create save directory if needed
    if args.save:
        os.makedirs(args.save_dir, exist_ok=True)

    # -------------------------------
    # IMAGE MODE
    # -------------------------------
    if not is_video:
        results = model(src, conf=args.conf)
        names = model.names
        img = draw_boxes(src, results, names, args.thickness)
        cv2.imshow("YOLOv8 Detection", img)

        if args.save:
            out_path = os.path.join(args.save_dir, "detected_image.jpg")
            cv2.imwrite(out_path, img)
            print(f"✅ Saved result to {out_path}")

        cv2.waitKey(0)

    # -------------------------------
    # VIDEO / WEBCAM MODE
    # -------------------------------
    else:
        cap = src
        print("🔵 Running YOLOv8 on video/camera feed (press 'q' to quit)...")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame, conf=args.conf)
            names = model.names
            img = draw_boxes(frame, results, names, args.thickness)

            cv2.imshow("YOLOv8 Detection", img)

            if args.save:
                frame_path = os.path.join(args.save_dir, "frame_detected.jpg")
                cv2.imwrite(frame_path, img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    print("✅ Detection completed successfully.")

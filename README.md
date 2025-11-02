# 🚀 Real-Time YOLOv8 Detection Script

This project provides a single, easy-to-use Python script (`detect.py`) for running real-time object detection using YOLOv8 models. It can process input from a webcam, video files, or static images and is highly configurable via command-line arguments.

[Image of detection results: A sample image with bounding boxes around detected objects like cars, people, etc.]

## ✨ Key Features

* **Multi-Source Input:** Works seamlessly with:
    * Webcam (`--source 0`)
    * Video files (`--source path/to/video.mp4`)
    * Image files (`--source path/to/image.jpg`)
* **Hardware Agnostic:** Automatically detects and uses your **NVIDIA GPU (CUDA)** if available, otherwise falls back to **CPU**.
* **Auto-Model Download:** If the specified model file (e.g., `yolov8n.pt`) isn't found, the script will automatically download it.
* **Save Results:** Easily save your detection results (annotated images or video frames) to disk using the `--save` flag.
* **Fully Configurable:** Adjust key detection parameters from the command line:
    * `--model`: Specify which YOLOv8 model file to use.
    * `--conf`: Set the confidence threshold for detections.
    * `--thickness`: Change the thickness of the bounding boxes.
    * `--save_dir`: Specify a custom directory for saved results.
* **Modern PyTorch Support:** Includes a built-in safety fix for loading models on **PyTorch 2.6+**.

---

## 🗂️ Project Structure

A simple and clean layout for running the script.


## 📦 Installation

1.  **Clone this repository (or just save the script):**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install the required packages:**
    Create a `requirements.txt` file with the following content:
    ```
    ultralytics
    torch
    torchvision
    opencv-python-headless
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Use

All commands are run from your terminal. The script will automatically find the best model weights (`best.pt`) from your training runs.

### 1. Run on a Webcam
This is the default action. It will use `yolov8n.pt` and a confidence of `0.25`.

```bash
python detect.py

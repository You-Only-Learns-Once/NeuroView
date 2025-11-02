
# 🎯 NeuroView


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)](https://github.com/ultralytics/ultralytics)

A **real-time multi-object detection system** powered by **YOLOv8** and **OpenCV**, capable of identifying and labeling multiple objects simultaneously in **images**, **videos**, or **live webcam feeds** with high precision.

---

## 🚀 Features

✅ **Accurate Multi-Object Detection** — Detects multiple objects in a single frame with optimized confidence filtering.  
✅ **Flexible Input Options** — Works with webcam, image, or video input.  
✅ **Safe Model Loading** — Fixes PyTorch 2.6+ serialization compatibility for secure model loading.  
✅ **Automatic Model Handling** — Auto-downloads YOLO weights if not found locally.  
✅ **GPU Acceleration** — Automatically uses CUDA if available for faster inference.  
✅ **Customizable Output** — Control confidence threshold, bounding box thickness, and save results easily.  
✅ **Lightweight & Modular** — Simple architecture ready for integration into larger AI pipelines.  

---

## 🧠 How It Works

1. Loads a YOLOv8 model (default: `yolov8n.pt`).
2. Accepts input from:
   - Webcam (`--source 0`)
   - Image files (`.jpg`, `.png`, etc.)
   - Video files (`.mp4`, `.avi`, etc.)
3. Performs real-time detection with bounding boxes and class labels.
4. Optionally saves detections to the `detections/` folder.

---

## ⚙️ Installation

bash
# Clone the repository
git clone https://github.com/yourusername/MultiObject-YOLOv8.git
cd MultiObject-YOLOv8

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On macOS/Linux

# Install dependencies
pip install -r requirements.txt
`

**requirements.txt**


ultralytics
torch
opencv-python


---

## ▶️ Usage

### Run on Webcam

bash
python detect.py --source 0


### Run on Image

bash
python detect.py --source path/to/image.jpg


### Run on Video

bash
python detect.py --source path/to/video.mp4


### Save Detected Output

bash
python detect.py --source 0 --save


### Adjust Confidence and Box Thickness

bash
python detect.py --source 0 --conf 0.4 --thickness 3


---

## 🧩 Project Structure


├── detect.py              # Main detection script
├── requirements.txt       # Python dependencies
├── detections/            # Auto-created folder for saved outputs
├── LICENSE                # MIT License
└── README.md              # Documentation (this file)


---

## 🧠 Model Notes

* Default model: `yolov8n.pt` (nano version for speed).
* You can replace it with any YOLOv8 variant:

  * `yolov8s.pt` (small)
  * `yolov8m.pt` (medium)
  * `yolov8l.pt` (large)
  * `yolov8x.pt` (extra-large)

---

## 🪄 Example Output

**Real-Time Detection Preview**


[INFO] Using device: cuda
🔵 Running YOLOv8 on video/camera feed (press 'q' to quit)...
✅ Detection completed successfully.


---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.


MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[Full MIT License text continues...]


---

## 🌟 Future Enhancements

* Add **object tracking (DeepSORT / ByteTrack)** for continuous detection across frames.
* Include **instance segmentation** and **object counting** modules.
* Integrate **audio alerts or region-based detection zones**.
* Build a **Streamlit dashboard** for visual analysis and logs.

---

## 🤝 Contributing

Contributions, pull requests, and feature ideas are welcome!
Feel free to open an issue or PR to make the model better.

---

## 💬 Acknowledgments

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* [PyTorch](https://pytorch.org/)
* [OpenCV](https://opencv.org/)


Would you like me to *personalize it* with your GitHub username, project name, and author details (for the MIT license and footer)?  
I can generate the complete version with those included next.
```

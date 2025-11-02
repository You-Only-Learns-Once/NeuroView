# 🚀 YOLOv8n Multi-Object Detection Project

This repository contains a lightweight, real-time multi-object detection model built using **YOLOv8 Nano (YOLOv8n)**. This project is optimized for high-speed performance on edge devices or in applications where computational resources are limited.

The model is trained to detect multiple custom object classes.



## 📋 Table of Contents

* [Features](#-features)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [Usage](#-usage)
    * [1. Dataset Preparation](#1-dataset-preparation)
    * [2. Model Training](#2-model-training)
    * [3. Run Inference](#3-run-inference)
    * [4. Model Validation](#4-model-validation)
* [Results](#-results)
* [Contributing](#-contributing)
* [License](#-license)
* [Acknowledgements](#-acknowledgements)

## ✨ Features

* **Lightweight:** Uses the YOLOv8n (Nano) model, the smallest and fastest in the YOLOv8 family.
* **Real-Time:** Capable of high-FPS object detection, suitable for video feeds and live cameras.
* **Multi-Class:** Trained to detect several custom object classes simultaneously.
    * Class 1: `[Your-Class-1]`
    * Class 2: `[Your-Class-2]`
    * Class 3: `[Your-Class-3]`
    * *(Add/remove as needed)*
* **Extensible:** Built on the `ultralytics` framework, making it easy to retrain, validate, and export.

## 🗂️ Project Structure

Here's the updated README with the dataset information included:

---

# Face Mask Detection Using YOLOv7

Welcome to the Face Mask Detection project! This repository contains code and resources to train and deploy a face mask detection model using the YOLOv7 architecture.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Inference](#inference)
- [Results](#results)
- [License](#license)

## Introduction
The aim of this project is to develop an efficient and accurate face mask detection system. Leveraging the YOLOv7 architecture, the model is capable of detecting whether individuals in images or videos are wearing face masks, making it highly applicable in real-world scenarios such as public health monitoring and security systems.

## Features
- **Real-time Detection**: Detects face masks in real-time using video streams.
- **High Accuracy**: Achieves high precision and recall using YOLOv7.
- **Scalable**: Can be deployed on various platforms.

## Dataset
The model is trained on the [Face Mask Detection Dataset](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection?resource=download) available on Kaggle. This dataset contains images of people with and without face masks, annotated for object detection tasks.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Douvakiing/yolov7-mask-detection
    cd face-mask-detection-yolov7
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    
## Usage
### Running Inference on Images
You can run inference on individual images to detect face masks:

```bash
python detect.py --source path/to/image.jpg --weights weights/yolov7.pt --conf-thres 0.5
```

### Running Inference on Videos
Similarly, you can run inference on videos:

```bash
python detect.py --source path/to/video.mp4 --weights weights/yolov7.pt --conf-thres 0.5
```

### Running Inference on Live Webcam
To perform real-time detection using a webcam:

```bash
python detect.py --source 0 --weights weights/yolov7.pt --conf-thres 0.5
```

## Inference
To evaluate the model on a test dataset:

```bash
python test.py --data data/face_mask.yaml --weights weights/best.pt
```

## Results
Here, you can showcase some results from your model, including images with detected face masks and performance metrics such as mAP, precision, and recall.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

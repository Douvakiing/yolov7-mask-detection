Here's the updated README with the dataset information included:

---

# Face Mask Detection Using YOLOv7

Welcome to the Face Mask Detection project! This repository contains code and resources to train and deploy a face mask detection model using the YOLOv7 architecture.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Introduction
This project aims to develop an efficient and accurate face mask detection system. Leveraging the YOLOv7 architecture, the model can detect whether individuals in images, videos, or camera feeds are wearing face masks, making it highly applicable in real-world scenarios such as public health monitoring and security systems.

## Dataset
The model is trained on the [Face Mask Detection Dataset](https://drive.google.com/file/d/1khxkAyETVO7QXlDNlbVFybsIupSAb2Ha/view?usp=sharing) which was derived from a dataset on [Kaggle](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection?resource=download) that was modified from Pascal VOC to YOLO format. This dataset contains images of people with and without face masks or wearing them incorrectly, annotated for object detection tasks.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Douvakiing/yolov7-mask-detection
    cd face-mask-detection-yolov7
    ```

2. **Install the required dependencies:**

   install [CUDA 11.3](https://developer.nvidia.com/cuda-11.3.0-download-archive)


    ```bash
    pip install -r requirements.txt
    pip install -r pytorch_install.txt
    ```
    
## Usage

### Running Inference on Live Webcam
To perform real-time detection using a webcam:

```bash
python detect.py --source 0 --weights (model-path) --conf-thres 0.5 --img-size 640 --view-img --no-trace
```

## Results
TODO

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

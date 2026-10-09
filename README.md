# AI-Based Waste Detection System Using YOLOv8

An AI-powered waste detection system built using a custom-trained YOLOv8 model to detect and localize different types of waste in images. The model identifies **Metal, Paper, Plastic, and Wet Waste** and draws bounding boxes around detected objects.

## Project Overview

This project uses computer vision and deep learning to detect waste objects automatically. It can be used as a starting point for smart waste segregation, waste monitoring, and environmental management applications.

### Features

- Detects four waste categories: Metal, Paper, Plastic, and Wet Waste.
- Uses a custom-trained YOLOv8 object detection model.
- Draws bounding boxes around detected objects.
- Supports predictions on individual images.
- Includes four sample images for testing.
- Saves annotated prediction images automatically.
- Includes model evaluation metrics from the test dataset.

## Technologies Used

- Python 3.11
- Ultralytics YOLOv8
- PyTorch
- OpenCV
- Roboflow dataset

## Supported Classes

| Class | Description |
|---|---|
| Metal | Metal waste and containers |
| Paper | Paper and paper-based waste |
| Plastic | Plastic bottles and other plastic waste |
| Wet Waste | Organic and food waste |

## Project Structure

```text
AI-Waste-Detection-YOLO/
├── models/
│   └── best.pt
├── test_images/
│   ├── metal.jpg
│   ├── paper.jpg
│   ├── plastic.jpg
│   └── wet_waste.jpg
├── predict.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Note:** The complete dataset, local Python virtual environment, and training outputs are not included in this repository. The trained model is included so users can run predictions without training it again.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sakshamjain9414/AI-Waste-Detection-YOLO.git
cd AI-Waste-Detection-YOLO
```

### 2. Create a Virtual Environment

For Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks environment activation, follow the appropriate Python environment activation instructions for your system.

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The project uses the Ultralytics package specified in `requirements.txt`. PyTorch and other required dependencies will be installed as dependencies where applicable.

For GPU acceleration, install a PyTorch build compatible with your NVIDIA GPU and CUDA setup. CPU inference is also possible, though it may be slower.

## How to Run Predictions

Run the following command from the project root directory.

### Test with the Sample Images

**Metal:**

```bash
python predict.py --source test_images/metal.jpg
```

**Paper:**

```bash
python predict.py --source test_images/paper.jpg
```

**Plastic:**

```bash
python predict.py --source test_images/plastic.jpg
```

**Wet Waste:**

```bash
python predict.py --source test_images/wet_waste.jpg
```

### Predict on Your Own Image

Place an image anywhere on your computer and provide its path:

```bash
python predict.py --source path/to/your/image.jpg
```

You can also change the confidence threshold. For example:

```bash
python predict.py --source test_images/plastic.jpg --conf 0.40
```

The default confidence threshold is `0.25`.

### Prediction Output

The script loads the trained model from `models/best.pt`, performs object detection, and saves an annotated image.

The output directory is:

```text
runs/predict/results/
```

Open the saved image to inspect the predicted classes, confidence scores, and bounding boxes.

## Model Evaluation

The custom-trained model was evaluated on the project's held-out test split.

| Metric | Test Result |
|---|---:|
| Precision | 87.4% |
| Recall | 88.6% |
| mAP@50 | 91.1% |
| mAP@50–95 | 69.5% |

These results are from the recorded evaluation run and may vary if the model, dataset, or evaluation settings change.

**Important:** The four included sample images are intended for demonstration. They are not sufficient to reproduce the overall evaluation metrics. A labelled test dataset is needed for an independent accuracy evaluation.

## Dataset

The model was trained using a Roboflow waste object-detection dataset containing four classes:

- Metal
- Paper
- Plastic
- Wet Waste

The original dataset contains approximately 4,624 images divided into training, validation, and test splits.

The complete dataset is not included in this repository. To retrain or independently evaluate the model, obtain the dataset from its original source and follow its applicable license and attribution requirements.

The original dataset export contained a mixture of bounding-box and segmentation annotations. The recorded Ultralytics training and evaluation runs used bounding boxes for detection.

## Limitations

- Prediction quality depends on the quality and variety of the training data.
- Performance may vary on images with poor lighting, unusual camera angles, or unfamiliar waste objects.
- The four sample images demonstrate inference but do not establish general accuracy.
- The model detects objects in images; it does not physically sort or collect waste.

## Future Improvements

- Expand the dataset with more diverse waste images.
- Improve performance on underrepresented classes.
- Build a real-time webcam detection interface.
- Develop a web application for image upload and prediction.
- Integrate the model with a smart waste segregation system.

## Author

**Saksham Jain**

GitHub: [Sakshamjain9414](https://github.com/Sakshamjain9414)

Project Repository: [AI-Waste-Detection-YOLO](https://github.com/Sakshamjain9414/AI-Waste-Detection-YOLO)

## License and Attribution

The project code and trained model are provided through this repository. Check the applicable licenses for the model dependencies and original dataset before redistributing them or using them commercially. Give the original dataset creator the attribution required by the dataset license.
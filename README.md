# AI-Based Waste Detection System using YOLOv8

An object detection project that uses a custom-trained YOLOv8 Nano model to identify four categories of waste: Metal, Paper, Plastic, and Wet Waste.

## Features

- Detects waste objects in images.
- Predicts four waste categories.
- Draws bounding boxes with class names and confidence scores.
- Uses a custom-trained YOLOv8n model.
- Supports image prediction through a command-line interface.

## Technologies Used

- Python 3.11
- Ultralytics YOLOv8
- PyTorch
- OpenCV
- Roboflow dataset

## Project Structure

```text
AI-Waste-Detection-YOLO/
├── models/
│   └── best.pt
├── predict.py
├── requirements.txt
├── .gitignore
├── README.md
└── thumb.jpg
```

The dataset, virtual environment, and generated training outputs are excluded from the repository.

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Waste-Detection-YOLO
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The default installation may use CPU inference. NVIDIA GPU acceleration requires a compatible CUDA-enabled PyTorch installation.

## Run Predictions

Place your image in the project folder or provide its full path.

```bash
python predict.py --source thumb.jpg
```

To change the confidence threshold:

```bash
python predict.py --source thumb.jpg --conf 0.40
```

The prediction output is saved to:

```text
runs/predict/results/
```

## Model Training

The custom model was trained for 50 epochs using a Roboflow waste object-detection dataset.

The dataset is not included in this repository. To retrain the model, download the dataset in YOLOv8 format, configure its `data.yaml` paths, and use the Ultralytics training command with an appropriate pretrained model.

## Evaluation Results

Reported test-split metrics:

| Metric | Score |
|---|---:|
| Precision | 87.4% |
| Recall | 88.6% |
| mAP@50 | 91.1% |
| mAP@50–95 | 69.5% |

These metrics were obtained on the project's test split. The dataset contains mixed detection and segmentation annotations, so results should be interpreted with that limitation in mind.

## Classes

1. Metal
2. Paper
3. Plastic
4. Wet Waste

## License and Dataset Attribution

The dataset's `data.yaml` identifies the dataset license as CC BY 4.0. Review the dataset's original license and attribution requirements before redistributing its images or annotations.

## Author

Developed as an AI-based waste object detection project using YOLOv8.
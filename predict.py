
from pathlib import Path
import argparse
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(
        description="AI-Based Waste Detection using YOLOv8"
    )
    parser.add_argument("--source", required=True, help="Image path")
    parser.add_argument("--conf", type=float, default=0.25)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    model_path = root / "models" / "best.pt"
    image_path = Path(args.source)

    if not image_path.is_file():
        raise FileNotFoundError(f"Image not found: {image_path}")

    model = YOLO(str(model_path))
    model.predict(
        source=str(image_path),
        conf=args.conf,
        save=True,
        project=str(root / "runs" / "predict"),
        name="results",
        exist_ok=True
    )

if __name__ == "__main__":
    main()

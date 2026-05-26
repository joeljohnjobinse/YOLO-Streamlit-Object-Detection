from ultralytics import YOLO
from pathlib import Path

class YOLOInference:

    def __init__(self):

        self.model = YOLO(
        "yolov8n.pt"
        )

    def process_directory(
        self,
        folder
    ):

        folder = Path(
        folder
        )

        metadata = []

        images = list(
        folder.glob("*")
        )

        for img in images:

            if img.suffix.lower() not in [
            ".jpg",
            ".png",
            ".jpeg"
            ]:
                continue

            results = self.model.predict(
            str(img)
            )

            result = results[0]

            detections=[]

            counts={}

            for box in result.boxes:

                cls = self.model.names[
                int(
                box.cls[0]
                )
                ]

                conf=float(
                box.conf[0]
                )

                detections.append(
                {
                "class":cls,
                "confidence":conf
                }
                )

                counts[cls]=counts.get(
                cls,
                0
                )+1

            metadata.append(
            {
            "image_path":
            str(img),

            "detections":
            detections,

            "class_counts":
            counts
            }
            )

        return metadata
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(image, confidence=0.4):

    results = model.predict(
        image,
        conf=confidence
    )

    result = results[0]

    output = result.plot()

    return output
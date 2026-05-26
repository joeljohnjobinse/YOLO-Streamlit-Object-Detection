# 🔍 Smart Visual Object Search System using YOLOv8 and Streamlit

# Name: Joel John Jobinse
# Register No: 212223240062

## 1. Project Title

**Smart Visual Object Search System using YOLOv8 and Streamlit**

---

## 2. Abstract / Introduction

This project presents a Computer Vision powered image search application developed using **YOLOv8**, **Streamlit**, and the **COCO dataset classes**.

Traditional image search systems rely on filenames or manual tagging. This project improves image retrieval by automatically detecting objects inside images and generating searchable metadata.

Users can:

- Process folders containing multiple images
- Detect objects using YOLOv8
- Store metadata automatically
- Search images using detected classes
- View matching images
- Export search results as JSON files

The application provides a simple interface for performing object-based visual searches and demonstrates practical usage of Computer Vision in image management systems.

---

## 3. Dataset & YOLO Model Details (COCO)

The project uses the pretrained **YOLOv8 Nano model (`yolov8n.pt`)** provided by Ultralytics.

YOLOv8 was trained using the **COCO (Common Objects in Context) dataset**.

COCO contains:

- 80 object classes
- Thousands of annotated images
- Bounding box information
- Object labels

Example detectable objects:

- Person
- Car
- Dog
- Cat
- Bicycle
- Bottle
- Chair
- Laptop
- Phone
- Bus
- Airplane
- Book

Model used:

```text
yolov8n.pt
```

YOLO Version:

```text
YOLOv8 Nano
```

Framework:

```text
Ultralytics YOLO
```

---

## 4. Environment Setup

Software Requirements:

- Python 3.10
- VS Code
- Anaconda Navigator
- Streamlit
- Ultralytics
- PyTorch

Project Structure:

```text
YOLO_Search_App/
│
├── app.py
├── requirements.txt
├── README.md
├── instruction.txt
├── .gitignore
│
├── src/
│   ├── inference.py
│   └── utils.py
│
├── uploads/
├── metadata/
│   └── results.json
│
├── outputs/
│
└── Screenshots/
```

---

## 5. CPU Installation Steps

Open **Anaconda Prompt**

Create environment:

```bash
conda create -n yolo_env python=3.10 -y
```

Activate environment:

```bash
conda activate yolo_env
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Verify installation:

```bash
python
```

Import YOLO:

```python
from ultralytics import YOLO
```

Exit:

```python
exit()
```

---

## 6. How to Run in VS Code using Conda

### Step 1

Open project folder in VS Code:

```text
File
→ Open Folder
→ YOLO_Search_App
```

### Step 2

Open terminal:

```text
Terminal
→ New Terminal
```

### Step 3

Activate Conda environment:

```bash
conda activate yolo_env
```

### Step 4

Run project:

```bash
streamlit run app.py
```

---

## 7. How to Deploy using Streamlit

The project is deployed locally using Streamlit.

Run:

```bash
streamlit run app.py
```

Default URL:

```text
http://localhost:8501
```

Features available:

✅ Folder image processing

✅ Object detection

✅ Metadata generation

✅ Search engine

✅ Search result display

✅ JSON export

---

## 8. Output Screenshots

### Conda Environment Activation

Insert screenshot:

```text
<img width="790" height="465" alt="image" src="https://github.com/user-attachments/assets/6116bc86-6ca6-4b07-9b0f-3dba275373f9" />

```

---

### Running Streamlit Command

Insert screenshot:

```text
<img width="1444" height="507" alt="image" src="https://github.com/user-attachments/assets/85b55698-ee11-4fe6-8ba0-4e15610f05ea" />

```

---

### Streamlit User Interface

Insert screenshot:

```text
Screenshots/ss4.png
```

---

### Object Detection Results

Insert screenshot:

```text
Screenshots/ss1.png
Screenshots/ss2.png
Screenshots/ss3.png
```

---

### Search Results

Insert screenshot:

```text
Screenshots/ss2.png
```

---

### 1. Visual Search Engine

Users can search images using object names.

Examples:

- Search person images
- Search cars
- Search phones
- Search multiple classes

---

### 2. Metadata Generation

The system automatically stores:

- Image path
- Detected objects
- Confidence values
- Object counts

---

### 3. JSON Export

Users can export search results for later usage.

---

### 4. Search Interface

Interactive image filtering through Streamlit UI.

---

### 5. COCO Integration

Uses pretrained YOLOv8 with support for 80 object categories.

---

## 10. Results & Conclusion

The developed Smart Visual Search System successfully performs object detection and image retrieval using YOLOv8.

The system was capable of:

- Detecting objects accurately
- Generating searchable metadata
- Returning matching images
- Exporting results
- Providing an interactive interface

The project demonstrates practical implementation of Computer Vision and Deep Learning techniques using Streamlit deployment.

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming |
| Streamlit | Web Interface |
| YOLOv8 | Object Detection |
| OpenCV | Image Processing |
| PyTorch | Deep Learning |
| COCO Dataset | Detection Classes |

---

## Author

Project developed for academic submission using:

- YOLOv8
- Streamlit
- COCO Dataset
- Python
- Anaconda Environment

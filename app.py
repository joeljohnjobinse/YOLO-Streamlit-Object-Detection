import streamlit as st
from pathlib import Path
import json

from src.inference import YOLOInference
from src.utils import (
    save_metadata,
    load_metadata,
    search_images
)

st.set_page_config(
    page_title="YOLO Search Engine",
    page_icon="🔍",
    layout="wide"
)

# ---------- SESSION ----------

if "metadata" not in st.session_state:
    st.session_state.metadata = []

if "results" not in st.session_state:
    st.session_state.results = []

# ---------- UI ----------

st.title(
    "🔍 Smart Visual Search Engine"
)

st.caption(
    "YOLOv8 + COCO Dataset Search System"
)

inferencer = YOLOInference()

mode = st.sidebar.radio(
    "Mode",
    [
        "Process Images",
        "Load Metadata"
    ]
)

# ---------- PROCESS ----------

if mode == "Process Images":

    folder = st.text_input(
        "Image Folder Path",
        "uploads"
    )

    if st.button(
        "Run Detection"
    ):

        with st.spinner(
            "Running YOLO..."
        ):

            metadata = inferencer.process_directory(
                folder
            )

            st.session_state.metadata = metadata

            save_metadata(
                metadata,
                "metadata/results.json"
            )

        st.success(
            f"{len(metadata)} images processed"
        )

# ---------- LOAD ----------

else:

    file = st.text_input(
        "Metadata Path",
        "metadata/results.json"
    )

    if st.button(
        "Load Metadata"
    ):

        if Path(file).exists():

            st.session_state.metadata = load_metadata(
                file
            )

            st.success(
                "Metadata loaded"
            )

# ---------- SEARCH ----------

metadata = st.session_state.metadata

if metadata:

    classes = sorted(
        list(
            {
                det["class"]

                for item in metadata

                for det in item[
                    "detections"
                ]
            }
        )
    )

    st.subheader(
        "Search Objects"
    )

    selected = st.multiselect(
        "Choose Classes",
        classes
    )

    if st.button(
        "Search"
    ):

        st.session_state.results = search_images(
            metadata,
            selected
        )

# ---------- DISPLAY ----------

results = st.session_state.results

if results:

    st.subheader(
        f"Results : {len(results)}"
    )

    cols = st.columns(3)

    idx = 0

    for item in results:

        with cols[idx]:

            st.image(
                item[
                    "image_path"
                ],
                use_container_width=True
            )

            st.json(
                item[
                    "class_counts"
                ]
            )

        idx = (idx + 1) % 3

    st.download_button(
        "Download JSON",
        data=json.dumps(
            results,
            indent=2
        ),
        file_name="results.json"
    )
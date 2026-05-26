import json
from pathlib import Path

def save_metadata(
metadata,
path
):

    Path(
    path
    ).parent.mkdir(
    exist_ok=True
    )

    with open(
    path,
    "w"
    ) as f:

        json.dump(
        metadata,
        f,
        indent=2
        )

def load_metadata(
path
):

    with open(
    path
    ) as f:

        return json.load(
        f
        )

def search_images(
metadata,
classes
):

    results=[]

    for item in metadata:

        detected=[
        x["class"]
        for x in item[
        "detections"
        ]
        ]

        if any(
        c in detected
        for c in classes
        ):

            results.append(
            item
            )

    return results
import os
import requests

BASE_PATH = "appointment/models"

MODELS = {
    "brain_tumor_model.h5": "https://mediflow-models.sgp1.digitaloceanspaces.com/brain_tumor_model.h5",
    "kidney_disease.h5": "https://mediflow-models.sgp1.digitaloceanspaces.com/kidney_disease.h5",
    "pneumonia.h5": "https://mediflow-models.sgp1.digitaloceanspaces.com/pneumonia.h5",
    "best.pt": "https://mediflow-models.sgp1.digitaloceanspaces.com/best.pt"
}

def download_models():

    os.makedirs(BASE_PATH, exist_ok=True)

    for name, url in MODELS.items():

        path = os.path.join(BASE_PATH, name)

        if not os.path.exists(path):

            print(f"Downloading {name}...")

            r = requests.get(url)

            with open(path, "wb") as f:
                f.write(r.content)

    print("All models ready.")
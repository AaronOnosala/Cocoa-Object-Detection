#importing libraries
import torch
from ultralytics import YOLO

if __name__ == '__main__':
    if torch.backends.mps.is_built() and torch.backends.mps.is_available():
        mps = torch.device("mps")
        # Load a model
        model = YOLO("yolov8n.yaml")  # build a new model from scratch

        # Use the model
        results = model.train(data="config.yaml", epochs=100)  # train the model


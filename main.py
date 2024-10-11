# Importing necessary libraries
import torch  # PyTorch library for tensor computations
from ultralytics import YOLOv10  # YOLO library for object detection models

if __name__ == '__main__':
    # Check if the Metal Performance Shaders (MPS) backend is available for PyTorch
    if torch.backends.mps.is_built() and torch.backends.mps.is_available():
        mps = torch.device("mps")  # Set the device to MPS (Apple's GPU acceleration)
        
        # Load a YOLO model configuration
        model = YOLOv10.from_pretrained("jameslahm/yolov10l")  # Build a new YOLO model from scratch using the specified configuration file

        # Train the model using the provided configuration file and number of epochs
        results = model.train(data="config.yaml", epochs=100)  # Train the model for 100 epochs

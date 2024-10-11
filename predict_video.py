# Importing necessary libraries
import os  # Library for interacting with the operating system
from ultralytics import YOLOv10 as YOLO # YOLO library for object detection models
import cv2  # OpenCV library for computer vision tasks

# Define the directory containing the video files
VIDEOS_DIR = os.path.join('.', 'videos')

# Define the input and output video paths
video_path = os.path.join(VIDEOS_DIR, 'alpaca1.mp4')
video_path_out = '{}_out.mp4'.format(video_path)

# Open the input video file
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()

# Get the height and width of the video frame
H, W, _ = frame.shape

# Define the video writer for the output video file
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Define the path to the trained YOLO model
model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'last.pt')

# Load the custom YOLO model
model = YOLO(model_path)

# Define the detection threshold
threshold = 0.5

# Process the video frames
while ret:
    # Perform object detection on the current frame
    results = model(frame)[0]

    # Iterate over the detected objects
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        # Draw bounding boxes and labels on the frame if the detection score is above the threshold
        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    # Write the processed frame to the output video file
    out.write(frame)
    
    # Read the next frame from the input video file
    ret, frame = cap.read()

# Release the video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()

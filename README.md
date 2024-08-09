# Cocoa-Object-Detection
## Background
The Cocoa Object Detection project aimed to create a robust model for identifying cocoa fruit at various stages 

1. __Mature_Unripe__ - Images with mature but not yet ripe cocoa pods
2. __Immature__ - Images with Cocoa pods that are still growing.
3. __Ripped__ - Images with ripe mature cocoa pods.
4. __Spoilt__ - Images with Spoilt cocoa pods.
![cocoa](https://github.com/user-attachments/assets/1f112077-0d8a-4637-8ab9-400ec9bcc4c0)

from images. The original dataset provided by [Makerere Artificial Intelligence Lab](https://air.ug) was in PASCAL VOC XML format, the dataset contains objects in cocoa trees under 4 classes Spoilt, Immature, Mature_Unripe and Ripped. It has been split into 3 subsets.

  * Train with 4550 images.
  * Validation with 1262 images.
  * Test with 318 images.
The dataset can be downloaded as a single zip file of ~370MB from [here.](https://storage.googleapis.com/air-lab-hackathon/Cocoa/cocoa_new.zip)
![cocoa_annotated](https://github.com/user-attachments/assets/d31614a5-030a-4a72-b46a-6ec572a11dd3)

The dataset has 2 types of labels. The first type is PASCAL VOC XML files for every image with the label information (see picture below) and these are found in the respective train and validation folders alongside the images. The second type of label is a CSV file named labelmap.csv that is found in the train and validation folders. A row in the CSV represents an object in the image and has 10 columns;

 + __Image id__ - The filename of the image in the respective folder. Note that this is repeated for images with multiple objetcs
 + __Actual Label__ - The class label of the objects of interest in the image.
 + __xmin, ymin, xmax, ymax__ - The bounding box cordinates of the objects in the image.
 + __xmin_norm, ymin_norm, xmax_norm, ymax_norm__ - The normalized bounding box coordinates of the objects in the image.
   
Image shows a sample PASCAL VOC annoation in XML format
<img width="921" alt="cocoa_xml_label" src="https://github.com/user-attachments/assets/f7688bf7-b498-4b1f-9b7b-6a8663670b79">

Image shows a sample of the labels in a CSV file for Cocoa
<img width="657" alt="cocoa_csv_label" src="https://github.com/user-attachments/assets/b84f22fe-920e-4141-ae4e-b7c1616742a3">

The challenge was to convert this data into a format suitable for training a YOLO (You Only Look Once) object detection model.

## Approach
## Data Preparation

 1. __Conversion:__ The original dataset annotations were in PASCAL VOC XML format. To train a YOLO model, we needed to convert these annotations into the YOLO format. This required writing a script to parse the XML files and convert bounding box coordinates and class labels into the YOLO format, which consists of normalized coordinates and class IDs.
 2. __Dataset Organization:__ The dataset was split into training, validation, and test subsets. The conversion script handled XML files in the train and validation folders, outputting YOLO-formatted text files.
    
## Model Building and Training:

 1. __Model Selection:__ YOLOv8 was selected for its efficiency and effectiveness in object detection tasks. The model configuration was adjusted to match the dataset's specifics.
   
 2. __Training:__ The model was trained on the converted dataset using the YOLO framework, with careful monitoring of performance metrics throughout the training process.
    
## Detection and Evaluation:

 1. __Inference:__ The trained model was applied to both images and videos to detect cocoa pods at various stages. Results were evaluated to ensure the model's accuracy and reliability in real-world scenarios.
 2. __Results Visualization:__ Detected objects were highlighted in the output video to visually assess the model's performance.





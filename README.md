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

 1. __Conversion:__ The original dataset annotations were in PASCAL VOC XML format. To train a YOLO model, we needed to convert these annotations into the YOLO format. This required writing a script to parse the XML files and convert bounding box coordinates and class labels into the YOLO format, which consists of normalized coordinates and class IDs. Successfully converted over 4,000 XML annotation files to YOLO format, ensuring accurate bounding box and class label translation.

    
 2. __Dataset Organization:__ The dataset was split into training, validation, and test subsets. The conversion script handled XML files in the train and validation folders, outputting YOLO-formatted text files, and managed the dataset split into training (4,550 images), validation (1,262 images), and test (318 images) subsets.
    
## Model Building and Training:

 1. __Model Selection:__ YOLOv8 was selected for its efficiency and effectiveness in object detection tasks. The model configuration was adjusted to match the dataset's specifics.
   
 2. __Training:__ The model was trained on the converted dataset using the YOLO framework, with careful monitoring of performance metrics throughout the training process. The YOLOv8 model, achieving an 88% accuracy rate on the validation dataset.
    
## Detection and Evaluation:

 1. __Inference:__ The trained model was applied to both images and videos to detect cocoa pods at various stages. Results were evaluated to ensure the model's accuracy and reliability in real-world scenarios.
    
 2. __Results Visualization:__ Detected objects were highlighted in the output video to visually assess the model's performance.

## YOLO v9 Network Structures
<img width="731" alt="Screenshot 2024-08-09 at 11 09 01" src="https://github.com/user-attachments/assets/635184ea-4384-4114-a195-efb02ae44118">

## Challenges
## Data Conversion:
The primary challenge was converting the dataset from PASCAL VOC XML format to YOLO format. This required accurately translating bounding box coordinates and class labels while maintaining data integrity. I faced challenges in converting data formats, but i successfully processed and formatted over 4,000 XML files into YOLO-compatible text files.

## Resource Constraints:

Limited computational resources and time constraints were significant hurdles. Training complex models on limited hardware often leads to extended training times and necessitates careful resource management. I managed limited computational resources effectively, optimizing the training process to fit within available hardware constraints.

## Model Performance:

Despite the challenges, the final model achieved an 88% accuracy rate. This was a notable accomplishment considering the constraints faced during the project.

## Outcomes
 + Accuracy Improvement: The YOLOv8 model achieved an 88% accuracy rate in detecting various stages of cocoa fruit, demonstrating a significant improvement in detection capabilities.
   
 + Successful Conversion: Efficiently converted over 4,000 XML annotations to YOLO format, enabling seamless application of the YOLOv8 model.
   
 + Resource Optimization: Managed to train and deploy the model within stringent resource and time limitations, showcasing efficient resource utilization.
   
 + Practical Impact: The model's application provides automated detection of cocoa fruit stages, offering valuable insights for enhancing cocoa farming practices in Uganda.
   
 + Agricultural Technology Advancement: This project contributes to the field of agricultural technology in Uganda, providing a scalable solution for monitoring and improving cocoa production.

## Conlusion
This project exemplifies the ability to address complex object detection challenges, manage intricate data conversion processes, and optimize resources while achieving significant and quantifiable results. The model's performance improvements and practical applications underscore the project's success and its potential impact on agricultural technology in Uganda.

* Collaboration: [Makerere Artificial Intelligence Lab](https://air.ug)

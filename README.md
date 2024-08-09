# Cocoa-Object-Detection
## Background
The Cocoa Object Detection project aimed to create a robust model for identifying cocoa fruit at various stages 

1. __Mature_Unripe__ - Images with mature but not yet ripe cocoa pods
2. __Immature__ - Images with Cocoa pods that are still growing.
3. __Ripped__ - Images with ripe mature cocoa pods.
4. __Spoilt__ - Images with Spoilt cocoa pods.
![cocoa](https://github.com/user-attachments/assets/1f112077-0d8a-4637-8ab9-400ec9bcc4c0)
from images. The original dataset was in PASCAL VOC XML format, the dataset contains objects in cocoa trees under 4 classes Spoilt, Immature, Mature_Unripe and Ripped. It has been split into 3 subsets.

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



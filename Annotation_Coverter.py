# Import the necessary libraries for XML parsing and file handling
from xml.dom import minidom
import os
import glob

# Create a look-up table (lut) for mapping class labels to numerical IDs
lut = {}
lut["Spoilt"] = 0
lut["Immature"] = 1
lut["Mature_Unripe"] = 2
lut["Ripped"] = 3

# Define the input and output directories for the dataset
input_dir = "/Users/aarononosala/Documents/Makerere/cocoa_new/train"
output_dir = "/Users/aarononosala/Documents/Makerere/cocoa_new/data/labels/train"

def convert_coordinates(size, box):
    """
    Convert bounding box coordinates from XML format to YOLO format.

    Args:
    size (tuple): A tuple containing the width and height of the image.
    box (tuple): A tuple containing the coordinates of the bounding box in XML format.

    Returns:
    tuple: A tuple containing the normalized coordinates of the bounding box in YOLO format.
    """
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_xml2yolo(lut):
    """
    Convert XML annotations to YOLO format.

    Args:
    lut (dict): Look-up table for class labels to numerical IDs.
    """
    # Iterate over all XML files in the input directory
    for fname in glob.glob(os.path.join(input_dir, "*.xml")):
        # Parse the XML file
        xmldoc = minidom.parse(fname)
        # Define the output file name
        fname_out = os.path.join(output_dir, os.path.basename(fname)[:-4] + '.txt')
        # Open the output file for writing
        with open(fname_out, "w") as f:
            # Get the list of objects (bounding boxes) in the XML file
            itemlist = xmldoc.getElementsByTagName('object')
            # Get the size of the image
            size = xmldoc.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)
            # Iterate over all objects in the XML file
            for item in itemlist:
                # Get the class label
                classid = (item.getElementsByTagName('name')[0]).firstChild.data
                if classid in lut:
                    label_str = str(lut[classid])
                else:
                    label_str = "-1"
                    print("warning: label '%s' not in look-up table" % classid)

                # Get the bounding box coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                # Convert the bounding box coordinates to YOLO format
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width, height), b)
                # Write the converted coordinates to the output file
                f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')
        # Print the name of the output file
        print("wrote %s" % fname_out)

def main():
    """
    Main function to start the conversion process.
    """
    convert_xml2yolo(lut)

# Run the main function if this script is executed
if __name__ == '__main__':
    main()

## Read in the pascal voc file and potentially alter to csv for this?
import os
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET

base_dir = '/Users/datascience4/Documents/training3'
print(len(os.listdir(base_dir)))
xml_files = os.listdir(base_dir)
print(xml_files)
items = []


for i in range(len(xml_files)):
    xml = os.path.join(base_dir, xml_files[i])
    tree = ET.parse(xml)
    root = tree.getroot()
    # path needs to be declared
    ## each row needs to look like this.
    ## path/to/img1.jpg xmin,ymin,xmax,ymax,class_id xmin,ymin,xmax,ymax,class_id
    ## path/to/img2.jpg xmin,ymin,xmax,ymax,class_id
    ## so each object in an image is only seperated by a space
    path = root.find('path').text
    ## make it a string for ease
    objects = ''
    for child in root.iter('object'):
        if child.find('bndbox'):
            bndbox = child.find('bndbox')
            xmin = bndbox.find('xmin').text
            ymin = bndbox.find('ymin').text
            xmax = bndbox.find('xmax').text
            ymax = bndbox.find('ymax').text
            objects += str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax) + ',classtobeadded! '
    print(objects)
    if bool(objects) == True:
        line = path + ' ' + objects + '\n'
        items.append(line)
    # print(items)



write_lines = open(os.path.join(base_dir, 'train.txt'), 'w')
for i in range(len(items)):
    write_lines.write(items[i])

write_lines.close()
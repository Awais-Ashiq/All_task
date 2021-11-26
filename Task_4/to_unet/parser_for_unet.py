import cv2, json, os
import numpy as np

def to_unet_format(path_to_json,path_to_masked,path_to_images):
    j_list=[]
    with open(path_to_json) as f: # Get data from Json
        j_dict = json.load(f)
    for val in j_dict.values():
        j_list.append([val['regions'], val['filename']])
        
    files = os.listdir(path_to_images)
    categories = []
    for index,img in enumerate(files):
        if img.endswith('g'):
            img1 = cv2.imread(f'{path_to_images}/{j_list[index][-1]}')
            mask = np.zeros(img1.shape,np.uint8)
            file_name = j_list[index][-1].split('.')[0]
            for classes in j_list[index][0]:
                
                x = classes['shape_attributes']['x']
                y = classes['shape_attributes']['y']
                w = classes['shape_attributes']['width']
                h = classes['shape_attributes']['height']
                
                name = classes['region_attributes']['names']
                categories.append(name) if name not in categories else categories
                color_val = categories.index(name)+1
                # print(img1.shape)
                font = cv2.FONT_HERSHEY_SIMPLEX
                # cv2.putText(img1,name, (x,y-5),font,1,[0,255,0],2)
                cv2.rectangle(mask,(x,y),(x+w,y+h), [color_val,color_val,color_val],-1)
                cv2.imwrite(f'{path_to_masked}/{file_name}.tiff', mask)

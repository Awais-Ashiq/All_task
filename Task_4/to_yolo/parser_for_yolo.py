import json
import os, cv2
# json path, dest to store txt file, images path directory 
def to_yolo_format(path_to_json,path_to_text_files,path_to_images):
    regions_list=[]
    with open(path_to_json) as f: # Get data from Json
        j_dict = json.load(f)
    for val in j_dict.values():
        regions_list.append([val['regions'], val['filename']])
        
    image_dir = os.listdir(path_to_images) # get list of all images name
    categories = []
    for index,img in enumerate(image_dir):
        if '.json' not in img:
            img1 = cv2.imread(f'{path_to_images}/{regions_list[index][-1]}')
            file_name = regions_list[index][-1].split('.')[0] # split image name from extension
            f = open(f'{path_to_text_files}/{file_name}.txt', 'w')
            for classes in regions_list[index][0]:
                
                x = classes['shape_attributes']['x']
                y = classes['shape_attributes']['y']
                w = classes['shape_attributes']['width']
                h = classes['shape_attributes']['height']
                x_max = x+w/2
                y_max = y+h/2
                x_center = (x_max)/img1.shape[1]
                y_center = (y_max)/img1.shape[0]
                width = w/img1.shape[1]
                height = w/img1.shape[0]
                name = classes['region_attributes']['names']
                categories.append(name) if name not in categories else categories
                f.write(f'{categories.index(name)} {x_center} {y_center} {width} {height}\n') # Write and store text files
            f.close()
    text_dir = os.listdir(path_to_text_files)
    success = True if len(text_dir) == len(image_dir) else False
    return success

# print(to_yolo_format('f.json','labels/','images/'))
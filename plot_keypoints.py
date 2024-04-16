import cv2
import random
import os
from tqdm import tqdm

def yolo_to_cv2_box(yolo_values, img_width, img_height):
    _, center_x, center_y, box_width, box_height = yolo_values
    
    # De-normalize the coordinates and dimensions
    x = int((center_x - box_width/2) * img_width)
    y = int((center_y - box_height/2) * img_height)
    width = int(box_width * img_width)
    height = int(box_height * img_height)
    
    return x, y, width, height

def plot_car(metadata_line, input_img):
        
        vehicle_types = {
            0: 'Compacts',
            1: 'Sedans',
            2: 'SUVs',
            3: 'Coupes',
            4: 'Muscle',
            5: 'Sports Classics',
            6: 'Sports',
            7: 'Super',
            8: 'Motorcycles',
            9: 'Off-road',
            10: 'Industrial',
            11: 'Utility',
            12: 'Vans',
            13: 'Cycles',
            14: 'Boats',
            15: 'Helicopters',
            16: 'Planes',
            17: 'Service',
            18: 'Emergency',
            19: 'Military',
            20: 'Commercial',
            21: 'Trains',
            22: 'Open Wheel',
        }

        rgb_values = [
            (255, 0, 0),   # Red
            (0, 255, 0),   # Green
            (0, 0, 255),   # Blue
            (255, 255, 0), # Yellow
            (255, 0, 255), # Magenta
            (0, 255, 255), # Cyan
            (128, 0, 0),   # Maroon
            (0, 128, 0),   # Green (Dark)
            (0, 0, 128),   # Navy
            (128, 128, 0), # Olive
            (128, 0, 128), # Purple
            (0, 128, 128), # Teal
            (255, 165, 0), # Orange
            (128, 128, 128), # Gray
            (255, 255, 255), # White
            (0, 0, 0),       # Black
            (192, 192, 192),  # Silver
            (255, 99, 71),    # Tomato
            (0, 128, 128),    # Dark Cyan
            (75, 0, 130),     # Indigo
            (255, 182, 193),  # Light Pink
        ]   
        rgb_values = [
            (255, 0, 0),     # Red
            (0, 255, 0),     # Green
            (0, 0, 255),     # Blue
            (255, 255, 0),   # Yellow
            (255, 0, 255),   # Magenta
            (0, 255, 255),   # Cyan
            (128, 0, 0),     # Maroon
            (0, 128, 0),     # Green (Dark)
            (0, 0, 128),     # Navy
            (128, 128, 0),   # Olive
            (128, 0, 128),   # Purple
            (0, 128, 128),   # Teal
            (255, 165, 0),   # Orange
            (128, 128, 128), # Gray
            (255, 255, 255), # White
            (0, 0, 0),       # Black
            (192, 192, 192),  # Silver
            (255, 99, 71),    # Tomato
            (0, 128, 128),    # Dark Cyan
            (75, 0, 130),     # Indigo
            (255, 182, 193),  # Light Pink
            (70, 130, 180),   # Steel Blue
            (255, 215, 0),    # Gold
        ]

        colour_white = (int(255), int(255), int(255))
        colour_red = (int(0), int(0), int(255))
        colour_green = (0, 255, 0)
        colour_random = [random.randint(0, 255) for _ in range(3)]
        colour_veh_class = rgb_values[int(metadata_line[0])] 

        metadata_list = metadata_line.split()
        metadata_list = [float(item) for item in metadata_list]

        b_box = metadata_list[:5]

        keypoints = metadata_list[5:]

        img_width =  input_img.shape[1]
        img_height = input_img.shape[0]
        
        x, y, width, height = yolo_to_cv2_box(b_box, img_width, img_height)
        cv2.rectangle(input_img, (x, y), (x + width, y + height), colour_veh_class, 2)
        
        area = width*height

        #print(area)
        if area >1000:
            label = f"{vehicle_types[int(b_box[0])]}"
            line_thickness = 1
            tl = line_thickness or round(0.002 * (input_img.shape[0] + input_img.shape[1]) / 2) + 1  # line/font thickness
            color = colour_veh_class
            c1, c2 = ((x, y), (x + width, y + height))
            tf = max(tl - 1, 1)  # font thickness
            t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
            c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
            cv2.rectangle(input_img, c1, c2, color, -1, cv2.LINE_AA)  # filled
            cv2.putText(input_img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

        keypoints_groups = [keypoints[i:i+3] for i in range(0, len(keypoints), 3)]
        all_coords = []
        for group in keypoints_groups:
            x,y,vis = group
            
            point_colour = colour_white if vis == 2 else colour_red
            
            point_size = int(area/500)
            point_size = 2 if point_size<2 else (5 if point_size>5 else point_size)
            new_x = int(x*img_width)
            new_y = int(y*img_height)
            current_points = (new_x, new_y)
            cv2.circle(input_img, current_points, point_size, point_colour, -1)
            all_coords.append(current_points)
        
        #bottom rectangle
        cv2.line(input_img, all_coords[0], all_coords[1], colour_red, 1)
        cv2.line(input_img, all_coords[1], all_coords[2], colour_red, 1)
        cv2.line(input_img, all_coords[2], all_coords[3], colour_red, 1)
        cv2.line(input_img, all_coords[3], all_coords[0], colour_red, 1)

        # Top rectangle
        cv2.line(input_img, all_coords[4], all_coords[5], colour_red, 1)
        cv2.line(input_img, all_coords[5], all_coords[6], colour_red, 1)
        cv2.line(input_img, all_coords[6], all_coords[7], colour_red, 1)
        cv2.line(input_img, all_coords[7], all_coords[4], colour_red, 1)

        # Bottom to top connection 
        cv2.line(input_img, all_coords[0], all_coords[4], colour_red, 1)
        cv2.line(input_img, all_coords[1], all_coords[5], colour_red, 1)
        cv2.line(input_img, all_coords[2], all_coords[6], colour_red, 1)
        cv2.line(input_img, all_coords[3], all_coords[7], colour_red, 1)

def plot_all_metadata(img_num):
    img = cv2.imread(f'{img_num}.jpg')

    with open(f'{img_num}.txt') as f:
        metadata_file = f.readlines()

    for line in metadata_file:
        plot_car(line, img)
        
    cv2.imshow("Bounding Box", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("output.jpg", img)

def plot_folder():
     
     target_folder = 'F:\Programming\Dissertation-mk2\dataset'
     os.makedirs(os.path.join(target_folder, 'annotated_images'), exist_ok=True)
     image_dir = os.path.join(target_folder, "images")
     label_dir = os.path.join(target_folder, "labels")

     for file in tqdm(os.listdir(image_dir)):
        current_item = file.split('.')[0]
        current_image = os.path.join(image_dir,current_item+'.jpg')
        current_label = os.path.join(label_dir,current_item+'.txt')

        img = cv2.imread(current_image)

        with open(current_label) as f:
            metadata_file = f.readlines()

        for line in metadata_file:
            plot_car(line, img)

        cv2.imwrite(os.path.join(target_folder, 'annotated_images', current_item+'.jpg'), img)
          


plot_folder()

#current_img = "38"
#plot_all_metadata(current_img)
    










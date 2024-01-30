import cv2

def yolo_to_cv2_box(yolo_values, img_width, img_height):
    _, center_x, center_y, box_width, box_height = yolo_values
    
    # De-normalize the coordinates and dimensions
    x = int((center_x - box_width/2) * img_width)
    y = int((center_y - box_height/2) * img_height)
    width = int(box_width * img_width)
    height = int(box_height * img_height)
    
    return x, y, width, height

def plot_car(metadata_line, input_img):
        metadata_list = metadata_line.split()
        metadata_list = [float(item) for item in metadata_list]

        b_box = metadata_list[:5]

        keypoints = metadata_list[5:]

        img_width =  input_img.shape[1]
        img_height = input_img.shape[0]

        x, y, width, height = yolo_to_cv2_box(b_box, img_width, img_height)
        cv2.rectangle(input_img, (x, y), (x + width, y + height), (0, 255, 0), 2)

        keypoints_groups = [keypoints[i:i+3] for i in range(0, len(keypoints), 3)]

        last_coords = None
        all_coords = []
        for group in keypoints_groups:
            x,y,vis = group
            colour_white = (int(255), int(255), int(255))
            colour_red = (int(0), int(0), int(255))
            point_colour = colour_white if vis == 2 else colour_red
            area = width*height
            point_size = int(area/500)
            point_size = 2 if point_size<2 else (5 if point_size>5 else point_size)
            new_x = int(x*img_width)
            new_y = int(y*img_height)
            current_points = (new_x, new_y)
            cv2.circle(input_img, current_points, point_size, point_colour, -1)
            all_coords.append(current_points)
            '''if last_coords is not None:
                print(f"{last_coords} to {(new_x,new_y)}")
                cv2.line(input_img, last_coords, (new_x,new_y), colour_red, 1)
            last_coords = current_points'''
        
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

    for file in metadata_file:
        plot_car(file, img)
        
    cv2.imshow("Bounding Box", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


current_img = "11"
plot_all_metadata(current_img)









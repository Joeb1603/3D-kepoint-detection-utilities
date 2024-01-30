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

        for group in keypoints_groups:
            x,y,vis = group
            colour_white = (int(255), int(255), int(255))
            colour_red = (int(0), int(0), int(255))
            point_colour = colour_white if vis == 2 else colour_red
            cv2.circle(input_img, (int(x*img_width), int(y*img_height)), 5, point_colour, -1)

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









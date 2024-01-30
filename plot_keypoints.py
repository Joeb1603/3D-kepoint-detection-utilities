import cv2

def yolo_to_cv2_box(yolo_values, img_width, img_height):
    _, center_x, center_y, box_width, box_height = yolo_values
    
    # De-normalize the coordinates and dimensions
    x = int((center_x - box_width/2) * img_width)
    y = int((center_y - box_height/2) * img_height)
    width = int(box_width * img_width)
    height = int(box_height * img_height)
    
    return x, y, width, height

img = cv2.imread('11.jpg')

img_width =  img.shape[1]
img_height = img.shape[0]

metadata = "2 0.5965937 0.6204128 0.09148418 0.1444954 0.5720473 0.6023851 1 0.5510744 0.6206424 2 0.618623 0.6931559 2 0.6396065 0.6689697 2 0.5733746 0.5489473 2 0.5520883 0.5652951 2 0.6211652 0.6306614 2 0.6424377 0.6088788 2"
metadata_list = metadata.split()
metadata_list = [float(item) for item in metadata_list]

b_box = metadata_list[:5]

keypoints = metadata_list[5:]

x, y, width, height = yolo_to_cv2_box(b_box, img_width, img_height)
cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)

keypoints_groups = [keypoints[i:i+3] for i in range(0, len(keypoints), 3)]


for group in keypoints_groups:
    #print(group)
    x,y,vis = group
    cv2.circle(img, (int(x*img_width), int(y*img_height)), 5, (int(255), int(255), int(255)), -1)

cv2.imshow("Bounding Box", img)
cv2.waitKey(0)
cv2.destroyAllWindows()







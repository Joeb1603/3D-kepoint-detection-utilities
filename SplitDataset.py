import os
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import natsort
import shutil

# TODO: Make it delete paths if they exist

# Set the directory path
annotations_path = os.path.join(os.getcwd(),'labels')
images_path = os.path.join(os.getcwd(),'images')

train_path = os.path.join(os.getcwd(),'yolov7','train')  # Add make if doesn't exist
test_path = os.path.join(os.getcwd(),'yolov7','test') # Add make if doesn't exist
validation_path = os.path.join(os.getcwd(),'yolov7','validation') # Add make if doesn't exist

# Create a dictionary to store the count for each class
class_counts = {}

annotations = os.listdir(annotations_path)
images = os.listdir(images_path)

print(f"{len(annotations)}=={len(images)}?")

"""images = natsort.natsorted(images)
print(images[0])
items = [0]
for thing2 in images:
    thing = thing2.split('.')[0]
    if int(thing)!=int(items[-1])+1:
        print(f"{thing} not {items[-1]+1}\nSOMETHING IS WRONG")
    items.append(int(thing))"""

if len(annotations)==len(images):
    images_train, images_test, annotations_train, annotations_test = train_test_split(images,annotations, test_size=0.2,train_size=0.8, random_state=42)
    images_train, images_validation, annotations_train, annotations_validation = train_test_split(images_train, annotations_train, test_size = 0.25,train_size =0.75, random_state=42)


    for image, annotation in zip(images_train, annotations_train):
        
        image_path = os.path.join(train_path,"images")
        if not os.path.exists(image_path):
            os.makedirs(image_path)

        annotation_path = os.path.join(train_path,"labels")
        if not os.path.exists(annotation_path):
            os.makedirs(annotation_path)

        #shutil.move(os.path.join(images_path,image), image_path)
        #shutil.move(os.path.join(annotations_path,annotation), annotation_path)

        shutil.move(os.path.join(images_path,image), os.path.join(train_path,"images",image))
        shutil.move(os.path.join(annotations_path,annotation), os.path.join(train_path,"labels",annotation))

    for image, annotation  in zip(images_test, annotations_test):

        image_path = os.path.join(test_path,"images")
        if not os.path.exists(image_path):
            os.makedirs(image_path)

        annotation_path = os.path.join(test_path,"labels")
        if not os.path.exists(annotation_path):
            os.makedirs(annotation_path)

        #shutil.move(os.path.join(images_path,image), image_path)
        #shutil.move(os.path.join(annotations_path,annotation), annotation_path)

        shutil.move(os.path.join(images_path,image), os.path.join(test_path,"images",image))
        shutil.move(os.path.join(annotations_path,annotation), os.path.join(test_path,"labels",annotation))

    for image, annotation  in zip(images_validation, annotations_validation):
        
        image_path = os.path.join(validation_path,"images")
        if not os.path.exists(image_path):
            os.makedirs(image_path)

        annotation_path = os.path.join(validation_path,"labels")
        if not os.path.exists(annotation_path):
            os.makedirs(annotation_path)

        #shutil.move(os.path.join(images_path,image), image_path)
        #shutil.move(os.path.join(annotations_path,annotation), annotation_path)

        shutil.move(os.path.join(images_path,image), os.path.join(validation_path,"images",image))
        shutil.move(os.path.join(annotations_path,annotation), os.path.join(validation_path,"labels",annotation))
        

    print(len(images_train)/len(images))
    print(len(images_test)/len(images))
    print(len(images_validation)/len(images))
    """
    class_names = {
        0: 'Compacts',  
        1: 'Sedans' ,
        2: 'SUVs' ,
        3: 'Coupes'  ,
        4: 'Muscle' ,
        5: 'Sports Classics' ,
        6: 'Sports' ,
        7: 'Super' ,
        8: 'Motorcycles'  ,
        9: 'Off-road' ,
        10: 'Industrial'  ,
        11: 'Utility'  ,
        12: 'Vans'  ,
        13: 'Cycles'  ,
        14: 'Boats'  ,
        15: 'Helicopters'  ,
        16: 'Planes'  ,
        17: 'Service'  ,
        18: 'Emergency'  ,
        19: 'Military'  ,
        20: 'Commercial'  ,
        21: 'Trains'  ,
        22: 'Open Wheel'

    }
    """

    """
    # Iterate over each file in the directory
    for filename in tqdm(os.listdir(annotations_path)):
        # Check if the file is a YOLO format text file
        if filename.endswith('.txt'):
            # Open the file and iterate over each line
            with open(os.path.join(annotations_path, filename), 'r') as f:
                for line in f:
                    # Extract the class label from the line
                    class_label = int(line.split(' ')[0])
                    # Increment the count for that class label in the dictionary
                    if class_label in class_counts:
                        class_counts[class_label] += 1
                    else:
                        class_counts[class_label] = 1

    # Print the count for each class label
    print(f"\n{'Class':<20}{'Instances'}\n")
    for class_label, count in class_counts.items():
        print(f"{class_names[class_label]:<20}{count}")
    print("\n")"""
else:
    print("Something wrong with dataset")
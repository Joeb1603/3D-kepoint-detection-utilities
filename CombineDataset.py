import os
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import natsort
import shutil

# TODO: Make it delete paths if they exist

# Set the directory path
annotations_path = os.path.join(os.getcwd(),'labels2')
images_path = os.path.join(os.getcwd(),'images2')

annotations_dest = os.path.join(os.getcwd(),'labels')
images_dest = os.path.join(os.getcwd(),'images')




annotations = os.listdir(annotations_path)
images = os.listdir(images_path)



for image, annotation in tqdm(zip(images, annotations)):
    
    new_id = (int(image.split('.')[0])+14420)
    shutil.move(os.path.join(images_path,image), os.path.join(images_dest,f"{new_id}.png"))
    shutil.move(os.path.join(annotations_path,annotation), os.path.join(annotations_dest,f"{new_id}.txt"))


    

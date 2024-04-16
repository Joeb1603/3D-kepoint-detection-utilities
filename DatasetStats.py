import os
from tqdm import tqdm

# Set the directory path
#dir_path = os.path.join(os.getcwd(),'labels')
dir_path = 'D:\\Dissertation\\dataset\\labels'
#dir_path = 'E:\\Dissertation\\dataset\\Dataset3\\annotations'

# Create a dictionary to store the count for each class
class_counts = {}

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


# Iterate over each file in the directory
for filename in tqdm(os.listdir(dir_path)):
    # Check if the file is a YOLO format text file
    if filename.endswith('.txt'):
        # Open the file and iterate over each line
        with open(os.path.join(dir_path, filename), 'r') as f:
            for line in f:
                # Extract the class label from the line
                class_label = int(line.split(' ')[0])
                # Increment the count for that class label in the dictionary
                if class_label in class_counts:
                    class_counts[class_label] += 1
                else:
                    class_counts[class_label] = 1

# Print the count for each class label
total = 0
print(f"\n{'Class':<20}{'Instances'}\n")
for class_label, count in class_counts.items():
    total += count
    print(f"{class_names[class_label]:<20}{count}")
print("")
print(f"{'Total vehicles:':20}{total}")
print("")
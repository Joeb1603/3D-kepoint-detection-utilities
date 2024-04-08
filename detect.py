from ultralytics import YOLO
from PIL import Image
import os 
# Load a model
model = YOLO('best.pt')  # load a tiger-pose trained model

# Run inference
results = model.predict(source="38.jpg")#, project="runs", name="",  save_txt=True)


output_path = (f"results.txt")

if os.path.exists(output_path):
    os.remove(output_path)

results[0].save_txt("results.txt")

im_array = results[0].plot()  # plot a BGR numpy array of predictions
im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
im.save('results.jpg')  # save image
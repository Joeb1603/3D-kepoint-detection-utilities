from ultralytics import YOLO



if __name__ == '__main__':

    # Load a model
    model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)

    # Train the model
    results = model.train(data='custom.yaml', epochs=300, imgsz=640, batch=64, project='runs')

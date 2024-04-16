import ultralytics
from ultralytics import YOLO



if __name__ == '__main__':


    file_path = ultralytics.utils.downloads.attempt_download_asset('yolov8n-pose.pt', repo='ultralytics/assets', release='latest')
    # Load a model
    model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)

    # Train the model
    results = model.train(data='custom.yaml', epochs=300, imgsz=640, batch=64, project='runs')

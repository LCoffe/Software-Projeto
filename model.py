from ultralytics import YOLO
from ultralytics import YOLO, settings

settings.update({'runs_dir': './runs'})

model = YOLO('yolov8n_custom.yaml')

model.train(data='custom_data.yaml',
            epochs=50,
            patience=300,
            batch=16,  # number of images per batch (-1 for AutoBatch)
            imgsz=640,
            workers=8,
            pretrained=True,
            resume=False,  # resume training from last checkpoint
            single_cls=False,  # Whether all classes will be the same (just one class)
            # project='runs/detect',  # Default = /home/{user}/Documents/ultralytics/runs
            box=7.5,  # More recall, better IoU, less precission, 
            cls=0.5,  # Bbox class better
            dfl=1.5,  # Distribution Focal Loss. Better bbox boundaries
            val=True,
            # Augmentations
            degrees=0.3,
            hsv_s=0.3,
            hsv_v=0.3,
            scale=0.5,
            fliplr=0.5)
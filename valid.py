from ultralytics import YOLO

model = YOLO('runs/detect/train10/weights/best.pt')

results = model.val(#project='runs/detect',
                    imgsz=640,
                    batch=16,
                    conf=0.001,
                    iou=0.7,  # Non-Maximum Supression (NMS)
                    save_json=False,  # Save to JSON {image_id, cls, bbox, conf} of each image in dataset
                    save_hybrid=False,  # Bounding box labels + inference on the output image (Ultralytics 8.0.178 = results are wrong when this argmunent is True)
                    split='test')  # train, val or test
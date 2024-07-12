from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # train a new model (based on nano model -> change last letter for other models, example yolov8s.yaml for small)
model.to('cuda') # for gpu training (NVIDIA only)

if __name__ == "__main__":
  # Train the model
  model.train( # settings in parameters -> see on official page for yolo
    data="config.yaml",
    epochs=150,
    seed = 45690,
    name = "Model_test",
    imgsz=640,
    patience = 15,
    batch = 16,
    workers = 6)  

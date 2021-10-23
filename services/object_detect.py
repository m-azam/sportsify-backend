from imageai.Detection import ObjectDetection
import os

def detect_object():
    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(os.path.join(execution_path, "yolo-tiny.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "cup-2.jpg"), output_image_path=os.path.join(execution_path , "cup-2-out.jpg"), minimum_percentage_probability=30)
detect_object()

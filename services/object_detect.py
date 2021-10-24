from imageai.Detection import ObjectDetection
import os
from PIL import Image
import math
import cv2

def detect_object():
    print('object detect called')
    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsTinyYOLOv3()
    print('object detect called')
    detector.setModelPath(os.path.join(execution_path + '/services/', "yolo-tiny.h5"))
    detector.loadModel(detection_speed="fast")
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path  + '/services/', "frame0.jpg"), output_image_path=os.path.join(execution_path , "services/output.jpg"), minimum_percentage_probability=30)
    
    
    image = Image.open("services/output.jpg")
    originalImage = cv2.imread("services/output.jpg")
    
    
    width, height = image.size
    centerx, centery = [width/2, height/2]
    print(f"dimensions -> {width}w, {height}h -- center points ({centerx}, {centery})")
    centered = lambda x1, y1, x2, y2: [(x2+x1)/2, (y2+y1)/2] 
    distance = lambda x1, y1, x2, y2: math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    Closets = []
    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        if Closets == []:
            center = centered(eachObject['box_points'][0], eachObject['box_points'][1], eachObject['box_points'][2], eachObject['box_points'][3])
            d = distance(center[0], center[1], centerx, centery)
            Closets = [eachObject["name"], d]
        else:
            center = centered(eachObject['box_points'][0], eachObject['box_points'][1], eachObject['box_points'][2], eachObject['box_points'][3])
            d = distance(center[0], center[1], centerx, centery)
            if d <= Closets[1]: Closets = [eachObject["name"], d]
        originalImage = cv2.circle(originalImage, (int(center[0]), int(center[1])), radius=0, color=(0, 0, 255), thickness=20)
        cv2.imwrite("services/saved-output1.jpg",originalImage)
        print(f"center points {center} and distance from center {d}")
        print("--------------------------------")
    print(Closets)
    
    return Closets[0]
    
    
def main():
    detect_object()
    
    
if __name__ == '__main__':
    main()
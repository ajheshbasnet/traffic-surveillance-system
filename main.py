import models
import cv2
from ultralytics import YOLO
from verify import fetch_details
from extractor import Detection
from database import engine

models.Base.metadata.create_all(bind = engine)

print("Starting....")

import cv2
import numpy as np

def main():

    model = YOLO(r'best.pt')
    cap = cv2.VideoCapture(r'images\test-video.mp4')
    detector = Detection(model)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
    out = cv2.VideoWriter("output_video.mp4", fourcc, 10, (1920, 1080))

    ret, frame = cap.read()

    while ret:
        if not ret or frame is None:
            break

        number_plates, bboxes = detector.predict(frame)
        
        for idx, number_plate in enumerate(number_plates):
            x1, y1, x2, y2 = bboxes[idx]
            message, status = fetch_details(number_plate)
            print(number_plate)
    
            if status == 1:                             #BGR
                cv2.rectangle(frame, (x1,y1), (x2,y2),(0, 0, 255), 4)
                cv2.rectangle(frame, (x1-35, y2+15), (x1+256 , y2+55), (0,0,0), thickness=-1)
                cv2.putText(frame, f"{message}", (x1-30, y2+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0, 255), 3)                

            elif status == 0:
                cv2.rectangle(frame, (x1,y1), (x2,y2),(0, 255, 0), 4)              
                cv2.rectangle(frame, (x1-30, y2+10), (x1+155 , y2+60), (20,20,20), thickness=-1)
                cv2.putText(frame, f"{message}", (x1-30, y2+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 3)

            else:
                cv2.rectangle(frame, (x1,y1), (x2,y2),(255, 0, 255), 4)    
                
        cv2.imshow("Frames", cv2.resize(frame, (960, 540)))
        out.write(frame)   
        ret, frame = cap.read()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break       

    cap.release()
    cv2.destroyAllWindows()
    print("Sucessfully Executed")

if __name__ == '__main__':
    main()
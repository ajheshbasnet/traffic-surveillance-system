import numpy as np
import cv2
import re
from database import get_db
import models
import easyocr

class Detection:

    def __init__(self, model):
        self.model = model
        self.easyocr = easyocr.Reader(['en'])
    

    def predict(self, resized_frame):
        db = get_db()
        THRESHOLD = 0.4

        results = self.model(resized_frame, stream = True, conf=0.5, iou=0.5)
        licence_plates = []
        for r in results:
            boxes = r.boxes
            bboxes = []
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                bboxes.append((x1, y1, x2, y2))               

                licence_plate_frame = resized_frame[y1:y2, x1:x2]

                licence_plate_frame = cv2.cvtColor(licence_plate_frame, cv2.COLOR_BGR2GRAY)

                ocr_results = self.easyocr.readtext(licence_plate_frame)
            
                lic_plate = []
                print(f'The type is: {type(ocr_results)}')
                
                if ocr_results:
                    for i in range(len(ocr_results)): 
                        bbox, licence_plate, ocr_conf = ocr_results[i]
                        licence_plate = licence_plate.lower()
                        
                        if ocr_conf > THRESHOLD:
                            lic_plate.append(licence_plate)
                    
                    licence_plate = ''.join(lic_plate)  

                    licence_plate = re.sub(r'[^a-z0-9]', '', licence_plate)
                    licence_plates.append(licence_plate)

                    user = db.query(models.Traffic_Database).filter(models.Traffic_Database.plate_no==licence_plate).first()
                    if user:
                        plate_no = user.plate_no
                        if licence_plate == plate_no:
                            w = len(plate_no) * 22
                            cv2.rectangle(resized_frame, (x1-10, y1-80), (x2+ w, y1-15), (0,0,0), thickness=-1)
                            cv2.putText(resized_frame, f"{licence_plate.upper()}", (x1-10, y1-15), cv2.FONT_HERSHEY_PLAIN, 4, (0,0, 255), 3)

        return licence_plates, bboxes
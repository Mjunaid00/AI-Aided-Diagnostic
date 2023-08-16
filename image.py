import cv2
from detection import ThroatDiseaseDetectionmodel
import numpy as np
import os

model = ThroatDiseaseDetectionmodel("model.json", 'model_weights.h5')
font = cv2.FONT_HERSHEY_SIMPLEX

def start_application():

    image_path = 'Images Folder/0iu5yjuk34567.JPG'
    #print(image_path)  # Check if the path is correct
    image = cv2.imread(image_path)

    #image = cv2.imread('pyringitus/5tdnhetgrjm.JPG')
    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(gray_frame, (250, 250))

    pred, prob = model.predict_disease(roi[np.newaxis, :, :])
    if pred == "infected throat":
        prob = round(prob[0][0] * 100, 2)

        # To beep when alert:
        # if prob > 90:
        #     os.system("say beep")

        cv2.rectangle(image, (0, 0), (280, 40), (0, 0, 0), -1)
        #cv2.putText(image, pred+ " " + str(prob), (20, 30), font, 1, (255, 0, 0), 2)
        cv2.putText(image, "Infected Throat", (20, 30), font, 1, (0, 0, 255), 2)
        print("It is an Infected Throat")
    else:
        cv2.putText(image, "Healthy Throat", (20, 30), font, 1, (0, 128, 0), 2)
        print("It is a Healthy Throat")
    cv2.imshow('Image', image)
    cv2.waitKey(0)

if __name__ == '__main__':
    start_application()

import cv2
from keras.models import model_from_json
import numpy as np
import tensorflow as tf
import logging

# Set TensorFlow logging level to only show errors
tf.get_logger().setLevel(logging.ERROR)

# Set logging level for keras to error
logging.getLogger('tensorflow').setLevel(logging.ERROR)

class FacialEmotionRecognition:
    def __init__(self, model_json_path, model_weights_path, haar_cascade_path):
        with open(model_json_path, "r") as json_file:
            model_json = json_file.read()
        self.model = model_from_json(model_json)
        self.model.load_weights(model_weights_path)
        self.face_cascade = cv2.CascadeClassifier(haar_cascade_path)
        self.labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}
        self.predic = ''
    def extract_features(self, image):
        feature = np.array(image)
        feature = feature.reshape(1, 48, 48, 1)
        return feature / 255.0

    def detect_emotions(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            image = gray[y:y + h, x:x + w]
            image = cv2.resize(image, (48, 48))
            img = self.extract_features(image)
            pred = self.model.predict(img)
            prediction_label = self.labels[pred.argmax()]
            self.predic = prediction_label
            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Put emotion label
            cv2.putText(frame, f'Emotion: {prediction_label}', (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))

        return frame
    
    def showPredic(self):
        return self.predic


# Usage example
# if __name__ == "__main__":
#     fer = FacialEmotionRecognition(
#         model_json_path=r"D:\Tugas\TA\MBKM RISET INDEPENDENT\Design Application\1\RTSP(Cameras)\fer.json",
#         model_weights_path=r"D:\Tugas\TA\MBKM RISET INDEPENDENT\Design Application\1\RTSP(Cameras)\fer.h5",
#         haar_cascade_path=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
#     )
#     video_path = r'C:\Users\Administrator\Documents\AceMovi Video Editor\Exported\Video_FER.avi'
#     fer.detect_emotions(0)

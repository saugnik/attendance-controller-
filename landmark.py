import os
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)

def extract_landmarks(image_path):
    """
    Extract facial landmarks from an image.
    """
    img = cv2.imread(image_path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_img)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            coords = [(int(landmark.x * img.shape[1]), int(landmark.y * img.shape[0]))
                      for landmark in face_landmarks.landmark]
            return coords
    return None

def visualize_landmarks(image_path, landmarks):
    """
    Visualize landmarks on the given image.
    """
    img = cv2.imread(image_path)
    for (x, y) in landmarks:
        cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

import os
import cv2

def preprocess_face(frame):
    """
    Preprocess the detected face.
    Crop, resize, and normalize the image.
    """
    face = cv2.resize(frame, (224, 224))  # Resize to model's input size
    face = face / 255.0  # Normalize pixel values to [0, 1]
    return face

def validate_dataset_path(dataset_dir):
    """
    Validate if the dataset directory exists and contains image files.
    """
    if not os.path.exists(dataset_dir):
        print(f"Error: Directory '{dataset_dir}' does not exist.")
        return False

    image_files = [f for f in os.listdir(dataset_dir)
                   if os.path.isfile(os.path.join(dataset_dir, f))
                   and f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'))]
    if not image_files:
        print(f"Error: No image files found in '{dataset_dir}'.")
        return False

    print(f"Found {len(image_files)} image files in '{dataset_dir}'.")
    return True

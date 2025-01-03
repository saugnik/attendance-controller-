import numpy as np
from tensorflow.keras.models import load_model

def load_trained_model(model_path):
    """
    Load the trained model.
    """
    return load_model(model_path)

def predict_face_class(model, face, class_names):
    """
    Predict the class of the given face.
    """
    prediction = model.predict(np.expand_dims(face, axis=0))
    return class_names[np.argmax(prediction)]

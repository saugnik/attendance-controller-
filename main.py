# sudo apt-get update
# sudo apt-get install python3-picamera


import cv2
from preprocessing import preprocess_face
from model import load_trained_model, predict_face_class
from attendance import initialize_csv, record_attendance
from picamera2 import Picamera2

# Configurations
MODEL_PATH = "attendance_recorder_model.h5"
CSV_PATH = "attendance.csv"
CLASS_NAMES = ['Hrithik', 'Srk', 'Salman', 'Saugnik']

# Load the trained model
model = load_trained_model(MODEL_PATH)

# Initialize attendance CSV
initialize_csv(CSV_PATH)

# Start the camera feed
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

while True:
    frame = picam2.capture_array()
    if not frame:
        break

    # Detect and preprocess face
    face = preprocess_face(frame)  # Ensure preprocess_face is implemented
    predicted_class = predict_face_class(model, face, CLASS_NAMES)

    # Log attendance
    record_attendance(predicted_class, CSV_PATH)

    # Display prediction
    cv2.putText(frame, f"Detected: {predicted_class}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Attendance Recorder', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()

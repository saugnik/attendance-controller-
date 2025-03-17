import cv2
from preprocessing import preprocess_face
from model import load_trained_model, predict_face_class
from attendance import initialize_csv, record_attendance

MODEL_PATH = "attendance_recorder_model.h5"
CSV_PATH = "attendance.csv"
CLASS_NAMES = ['Hrithik', 'Srk', 'Salman', 'Saugnik']

model = load_trained_model(MODEL_PATH)
initialize_csv(CSV_PATH)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    face = preprocess_face(frame)
    predicted_class = predict_face_class(model, face, CLASS_NAMES)

    record_attendance(predicted_class, CSV_PATH)

    cv2.putText(frame, f"Detected: {predicted_class}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Attendance Recorder', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

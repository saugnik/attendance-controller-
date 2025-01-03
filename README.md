<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Attendance Recorder Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        header {
            text-align: center;
            background-color: #282c34;
            color: #fff;
            padding: 20px 0;
        }
        header h1 {
            margin: 0;
        }
        section {
            padding: 20px;
            margin: 20px;
        }
        h2 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 8px 0;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        footer {
            text-align: center;
            padding: 20px;
            background-color: #282c34;
            color: #fff;
        }
    </style>
</head>
<body>
    <header>
        <h1>Attendance Recorder Project</h1>
        <p>AI-based facial recognition system for recording attendance using TensorFlow and OpenCV.</p>
    </header>

    <section>
        <h2>Project Description</h2>
        <p>This project implements an automated attendance recorder system using facial recognition. The system is built using TensorFlow and OpenCV, and it classifies students based on their facial features.</p>
        <p>Key components of the project:</p>
        <ul>
            <li>Facial Recognition using MobileNetV2</li>
            <li>Training with a custom dataset</li>
            <li>Attendance recording using CSV</li>
            <li>Real-time detection using OpenCV and Camera Feed</li>
        </ul>
    </section>

    <section>
        <h2>Getting Started</h2>
        <p>Follow these steps to get the project up and running on your local machine:</p>
        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.x</li>
            <li>TensorFlow</li>
            <li>OpenCV</li>
            <li>CSV File for attendance data</li>
        </ul>
        <h3>Installation</h3>
        <pre>
            # Clone the repository
            git clone https://github.com/saugnik/attendance-recorder.git

            # Install dependencies
            pip install tensorflow opencv-python pandas mediapipe
        </pre>
        <h3>Directory Structure</h3>
        <ul>
            <li><code>attendance_recoder.v1i.multiclass/train/</code> - Training images and dataset</li>
            <li><code>attendance_recoder.v1i.multiclass/valid/</code> - Validation images and dataset</li>
            <li><code>attendance_recorder_model.h5</code> - Trained model</li>
            <li><code>attendance.csv</code> - Records of attendance</li>
        </ul>
    </section>

    <section>
        <h2>Usage</h2>
        <p>After setting up the project, run the following Python script to start the attendance recording system:</p>
        <pre>
            python attendance_recorder.py
        </pre>
        <p>This script will:</p>
        <ul>
            <li>Load the trained model</li>
            <li>Start the camera feed</li>
            <li>Perform facial recognition and classify the faces</li>
            <li>Record attendance in the <code>attendance.csv</code> file</li>
        </ul>
    </section>

    <section>
        <h2>Code Explanation</h2>
        <p>This section explains the key components of the code:</p>
        <h3>Image Preprocessing</h3>
        <p>The images are resized to 224x224 pixels and processed using TensorFlow's <code>image_dataset_from_directory</code> for training and validation datasets.</p>
        <h3>Model Training</h3>
        <p>A MobileNetV2 model is used as the base model, with a custom classification layer on top to classify faces into students.</p>
        <h3>Attendance Recording</h3>
        <p>When a face is recognized, the student's name is recorded in the <code>attendance.csv</code> file with a timestamp.</p>
    </section>

    <section>
        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <a href="https://opensource.org/licenses/MIT" target="_blank">LICENSE</a> file for details.</p>
    </section>

    <footer>
        <p>&copy; 2025 Attendance Recorder Project. All Rights Reserved.</p>
    </footer>
</body>
</html>

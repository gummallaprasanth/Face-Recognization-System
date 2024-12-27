# Face Recognition System

This is a face recognition system implemented using OpenCV and Python. The system is designed to detect and recognize faces in images . It can be trained with a set of labeled face images and used to predict the identity of a face in real-time.

## Features

Face Detection: Detect faces in images.

Face Recognition: Train a model using labeled face images and recognize faces in real-time.

Real-time Camera Feed: Use the system with a webcam for live face recognition.

Training System: Allows adding new faces and updating the training model.

## Requirements

Python 4.5.2

OpenCV (opencv-python)

Numpy

(Optional) Other dependencies for your specific dataset

## Setup

### 1. Collecting Training Data

Before using the face recognition system, you need to collect images for training.

Navigate to the data/ folder (or create one in your project).

Use the collect_images.py script to capture face images for each person.

### 2. Train the Recognizer

Once you have collected sufficient face images, you need to train the recognizer. Use the train_demo.py script for this.
This script will load the collected face data, train the recognizer, and save the trained model as trainer.yml for later use.

### 3. Running the Face Recognition

After training, you can use the recognize_faces.py script to start real-time face recognition using your webcam.
The program will open the webcam feed, detect faces in real-time, and attempt to recognize any detected faces based on the trained model.

### 4. Adding New Faces
To add new faces to the system, simply capture new images using the collect_images.py script and retrain the model using the train_demo.py script.

## Acknowledgements

OpenCV: For the face detection and recognition functionalities.

Python: For the easy-to-use language that powers this system.

Any additional libraries or datasets you used for training or testing.

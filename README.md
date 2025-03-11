### 🏆 Repository Name
Hand-Detection-OpenCV-Mediapipe

## 📄 Description
This project implements real-time hand detection using OpenCV and MediaPipe in Python. It captures video from a webcam, processes hand landmarks, and visualizes them using OpenCV. The MediaPipe framework is used to detect and track hand landmarks efficiently, making it suitable for gesture recognition, hand movement analysis, and interactive applications.

## 🚀 Features
✅ Real-time hand detection using OpenCV and MediaPipe
✅ Draw hand landmarks with customizable color and thickness
✅ Efficient and fast processing using GPU if available
✅ Clean and modular code structure

## 🏗️ Installation
Clone the repository
git clone https://github.com/ABILASHGOVINDH/Hand-Detection-OpenCV-Mediapipe.git

# Navigate to the project directory
cd Hand-Detection-OpenCV-Mediapipe

# Create a virtual environment (Optional)
python -m venv venv
source venv/bin/activate   # On Windows use: .\venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

# 🎯 Usage
Run the script
python hand_detection.py

## Controls
Press 'q' – Quit the application
🖥️ Code Structure


# 📂 Hand-Detection-OpenCV-Mediapipe
├── hand_detection.py   # Main hand detection script
├── requirements.txt    # List of dependencies
├── README.md   # Project documentation

## 🏅 How It Works
Captures live video feed using cv.VideoCapture(0)
Converts the frame to RGB format
Detects hand landmarks using MediaPipe Hands
Draws landmarks and connections using OpenCV


## 🌐 Dependencies
Python 3.8+
OpenCV
MediaPipe

## 🙏 Acknowledgments
MediaPipe – For providing a powerful framework for real-time hand tracking
OpenCV – For efficient image processing
🔗 References
# 📖 MediaPipe Documentation – https://developers.google.com/mediapipe
# 📖 OpenCV Documentation – https://docs.opencv.org

## 📌 Contributing
Fork the repository
Create a new branch (git checkout -b feature/branch)
Commit changes (git commit -m "Add new feature")
Push to the branch (git push origin feature/branch)
Open a Pull Request

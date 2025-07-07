# 👁️ Eye Detection and Blinking Counter using OpenCV, Mediapipe & cvZone

Hello Everyone 

Check out this fun and fascinating Computer Vision project — **Eye Detection and Blinking Counter**! Built using **OpenCV**, **Mediapipe**, and the **cvZone** framework, this project detects your eyes in real-time and counts how many times you blink. 

---

## 🔧 Technologies Used

- **OpenCV**: Real-time computer vision library.
- **Mediapipe** (via cvZone): For facial landmark detection (FaceMesh).
- **cvZone**: A wrapper over OpenCV and Mediapipe that simplifies computer vision tasks.

---

## 🎯 Project Goal

To track human eye movement using facial landmarks and count how many times a person blinks — in real time or from a video file.

---

## 🧠 How It Works

- The script loads a video and uses the **FaceMeshDetector** from `cvzone` to identify 12 eye landmarks.
- It calculates the **vertical-to-horizontal ratio** of eye dimensions using Euclidean distance.
- A blink is counted when the ratio drops below a threshold (~31%) and rebounds, indicating a closed-and-open action.

### 🔍 Key Code Snippet:

```python
leftUp = face[159]
leftdown = face[23]
leftLeft = face[130]
leftRight = face[243]

lengthVar, _ = detector.findDistance(leftUp, leftdown)
lengthHor, _ = detector.findDistance(leftLeft, leftRight)

ratio = (float(lengthVar / lengthHor) * 100)
ratioList.append(ratio)

# Blink detection logic
if (ratioAvg < 31 and counter == 0):
    blinkCounter += 1
    counter = 1
```
🚀 Getting Started
✅ Requirements:
Python 3.x

OpenCV

Mediapipe

cvzone

Install dependencies:
```
pip install opencv-python mediapipe cvzone
```
Make sure to replace the video path if you're using a local video:

python
```
cap = cv2.VideoCapture("E:\\Video\\python_project_Videos\\eye_blinking.mp4")
```
 Applications
This type of eye-blink detection can be applied in:

👨‍⚕️ Healthcare: Fatigue detection, sleep apnoea monitoring

🧠 Research: Psychology, neuroscience, human behavior

💻 HCI: Gaze-based UI control

🚗 Safety: Driver drowsiness detection

🔒 Security: Real-time surveillance analytics


📖 References & Inspirations
Mediapipe Documentation

cvZone by Murtaza Hassan

GeeksforGeeks Eye Blink Detection

Sample blinking video: Eye Blinking Girl


🙌 Acknowledgments
Thanks to:

Murtaza's Workshop – Robotics & AI

GeeksforGeeks.org


























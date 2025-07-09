# 🖱️ AI-Based Virtual Mouse using Hand Gestures

A Python-based system that uses **computer vision** and **hand gesture recognition** to control your mouse and system volume — no physical mouse required. Built using **OpenCV**, **MediaPipe**, and **Python**, this project showcases the power of Human-Computer Interaction (HCI) using only a webcam.

---

## 📌 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Demo](#demo)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Technical Overview](#technical-overview)
- [Accuracy & Testing](#accuracy--testing)
- [Contributors](#contributors)
- [License](#license)

---

## 🚀 Features

- 🖱️ Virtual Mouse:
  - All functions of physical mouse are achieved using hand gestures
- 🔊 Volume Control:
  - Adjust volume using distance between thumb and index finger
- 🎯 Real-time performance with FPS overlay
- 📷 Works with basic webcam

---

## 🗂 Project Structure

| File                | Description                                          |
|---------------------|----------------------------------------------------- |
| `tracking_module.py` | Core hand tracking and gesture processing logic     |
| `AI_mouse.py`        | Mouse movement and click using gestures             |
| `volume_control.py`  | Volume control based on finger distance             |
| `main_module.py`     | Basic MediaPipe demo (for testing webcam setup)     |
| `requirements.txt`   | List of required Python packages                    |
| `assets/`            | Screenshots                                         |

---

## 🎥 Demo

> Add screenshots or gifs here from `assets/` folder

![AI Mouse Demo](assets/mouse_demo.gif)

---

## 💻 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/ai-virtual-mouse.git
   cd ai-virtual-mouse

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Ensure Webcam Access**
   Change camera index to 0 or 1 in .py files if needed

## 🧑‍💻 How to Use

➤ Virtual Mouse
   ```bash
    python AI_mouse.py
```
➤ Volume Control
```bash
    python volume_control.py
```
➤ Webcam + Hand Detection Test
```bash
  python main_module.py
```
✨ Tip: If webcam doesn’t open, try changing cv2.VideoCapture(1) to cv2.VideoCapture(0)

## 🧠 Technical Overview

Libraries Used:
-> OpenCV – for image processing and camera handling
-> MediaPipe – for hand landmark detection
-> Numpy – numerical operations
-> Autopy – to control mouse cursor
-> Pycaw – to manage system volume
-> Comtypes – support for Windows COM library

## Gesture Mapping:

| Gesture                             | Action                                              |
|-------------------------------------|-----------------------------------------------------|
| Index Finger Up                     | Mouse Movement                                      |
| Index + Middle Finger Up            | Right Button Click                                  |
| Index, Middle, Little Finger Up     | Left Button Click                                   |
| Thumb, Index, Middle, Little Up     | Scroll Up Function                                  |
| Thumb, Index, Middle Up             | Scroll Down Function                                |
| No Tip Detected                     | No Action Performed                                 |
| Thumb + Index Pinch (distance)      | Volume Control based on Finger Distance             |

## 📊 Accuracy & Testing

| Gesture         | Accuracy |
| --------------- | -------- |
| Cursor Movement | 100%     |
| Left Click      | 99%      |
| Right Click     | 98%      |
| Scroll Up/Down  | 100%     |

## Lighting Test Accuracy

| Lighting Condition | Accuracy |
| ------------------ | -------- |
| Daylight           | 93%      |
| Dim Light          | 70%      |
| Night Light        | 40%      |

## 📄 License
This project is for educational and research purposes. Feel free to fork and contribute.

## 🙌 Acknowledgements
  -> MediaPipe by Google
  -> OpenCV
  -> pycaw documentation



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

1. Left Click
   
   ![Left Click](https://github.com/user-attachments/assets/d34a7e85-9f69-42e4-b2f4-2676d99bbf68)


2. Right Click
   
   ![Right Click](https://github.com/user-attachments/assets/3b42b5f4-9832-4beb-8ae4-4aa545e231a2)


3. Scroll Up
   
   ![Scroll Up](https://github.com/user-attachments/assets/f036a372-ad0a-49d7-b208-ed45cd5fbb68)

   
4. Scroll Down
   
   ![Scroll Down](https://github.com/user-attachments/assets/b7058535-dd4a-49cf-b302-d2a10c789174)


5. Volume Decrease

   ![Volume Decrease](https://github.com/user-attachments/assets/8969d672-e750-4191-a35d-774a2b702fdd)


6. Volume Increase
  
   ![Volume Increase](https://github.com/user-attachments/assets/90109099-748c-4d3c-b318-b8a0be954ed9)


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

---

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

---

## 🧠 Technical Overview

Libraries Used:
-> OpenCV – for image processing and camera handling
-> MediaPipe – for hand landmark detection
-> Numpy – numerical operations
-> Autopy – to control mouse cursor
-> Pycaw – to manage system volume
-> Comtypes – support for Windows COM library

---

## Gesture Mapping:

| Gesture                                | Action                                              |
|----------------------------------------|-----------------------------------------------------|
| Index Finger Up                        | Mouse Movement                                      |
| Index, Middle Finger Up                | Right Button Click                                  |
| Index, Middle, Little Finger Up        | Left Button Click                                   |
| Thumb, Index, Middle, Little Finger Up | Scroll Up Function                                  |
| Thumb, Index, Middle Finger Up         | Scroll Down Function                                |
| No Tip Detected                        | No Action Performed                                 |
| Thumb, Index Finger Pinch (distance)   | Volume Control based on Finger Distance             |

---

## 📊 Accuracy & Testing

| Gesture         | Accuracy |
| --------------- | -------- |
| Cursor Movement | 100%     |
| Left Click      | 99%      |
| Right Click     | 98%      |
| Scroll Up/Down  | 100%     |

---

## Lighting Test Accuracy

| Lighting Condition | Accuracy |
| ------------------ | -------- |
| Daylight           | 93%      |
| Dim Light          | 70%      |
| Night Light        | 40%      |

---

## 📄 License
This project is for educational and research purposes. Feel free to fork and contribute.

---

## 🙌 Acknowledgements

  -> MediaPipe by Google
  -> OpenCV
  -> pycaw documentation

---

## 🙋‍♀️ About Me

**Kirti Jeswani**  
Data Analyst | Data Engineer  
🔗 [LinkedIn](https://www.linkedin.com/in/kirti-jeswani/)  
📧 kirti.jeswani23@gmail.com

---

## ⭐ Like This Project?

Star ⭐ this repo and connect with me on LinkedIn. Feedback and contributions are always welcome!




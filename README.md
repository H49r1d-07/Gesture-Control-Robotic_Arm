# Gesture-Controlled Robotic Arm

This project demonstrates a real-time hand gesture controlled robotic arm using Python, OpenCV, and Arduino. 
Hand gestures captured through a webcam are processed using computer vision and translated into physical finger movements via servo motors.

---

## Problem Statement
Traditional robotic control methods rely on buttons or joysticks, which are not intuitive. 
This project enables natural human–machine interaction by allowing users to control a robotic hand using simple hand gestures.

---

## Tech Stack
- Python
- OpenCV
- MediaPipe
- Arduino
- Servo Motors
- Serial Communication

---

## System Architecture
1. Webcam captures real-time video
2. MediaPipe detects hand landmarks
3. Gesture logic converts landmarks into finger states
4. Python sends gesture data via serial communication
5. Arduino receives data and controls servo motors

---

## Hardware Setup
![Robotic Hand Setup](assets/robotic_hand_setup.jpg)

The hardware consists of a 3D-printed robotic hand with servo motors controlled by an Arduino board.

---

## Performance Optimization
- Reduced unnecessary frame processing
- Sent data to Arduino only when gesture state changes
- Improved response time and stability
- Achieved smoother real-time control

---

## How to Run

### Python Side
```bash
pip install -r requirements.txt
python src/main.py

# Gesture-Controlled Robotic Arm

This project implements a **real-time hand gesture controlled robotic arm** using **Python, OpenCV, MediaPipe, and Arduino**.  
Hand gestures captured via a webcam are processed using computer vision and translated into physical finger movements using servo motors.

The goal of this project is to enable **natural and intuitive human–machine interaction** without using buttons, joysticks, or switches.

---

## Problem Statement
Traditional robotic control methods rely on physical interfaces that are not intuitive or flexible.  
This project solves that problem by allowing users to **control a robotic hand using simple hand gestures**, making interaction more natural and user-friendly.

---

## Tech Stack

### Software
- Python
- OpenCV
- MediaPipe
- PySerial

### Hardware
- Arduino (Uno / Nano)
- Servo Motors
- Robotic Hand
- Webcam

---

## System Workflow
1. Webcam captures real-time video
2. MediaPipe detects hand landmarks
3. Finger states are calculated from landmark positions
4. Gesture data is encoded as binary values
5. Python sends data to Arduino via serial communication
6. Arduino controls servo motors
7. Robotic hand mimics human gestures in real time

---

## Python Implementation

The Python program handles **computer vision and gesture detection**.

### Key Responsibilities
- Capture live video using OpenCV
- Detect hand landmarks using MediaPipe
- Identify finger states (open / closed)
- Send gesture data to Arduino through serial communication

### Gesture Encoding Format
Each hand gesture is encoded as a **5-bit binary string**, where:

- `1` → Finger open  
- `0` → Finger closed  

Example:


- Each digit represents a finger (Thumb → Little finger)
- `*` is used as an end-of-data marker
- Data is sent only when the gesture changes (performance optimization)

---

## Arduino Implementation

The Arduino program receives gesture data from Python and controls the servo motors.

### Responsibilities
- Read serial data from Python
- Decode finger state values
- Rotate servo motors accordingly
- Ensure smooth and synchronized finger movement

### Servo Pin Mapping

| Finger  | Arduino Pin |
|--------|-------------|
| Thumb  | 3 |
| Index  | 5 |
| Middle | 6 |
| Ring   | 9 |
| Little | 10 |

Arduino processes the gesture only after receiving the `*` character.

---

## Hardware Setup

The hardware consists of a robotic hand with servo motors connected to an Arduino board.  
Each servo corresponds to one finger of the robotic hand and moves based on detected hand gestures.

(Actual hardware image is included in the repository assets.)

---

## Performance Optimization
- Reduced unnecessary frame processing
- Sent serial data only when gesture state changes
- Improved response time between gesture and movement
- Achieved smoother and more stable real-time control

---

## How to Run the Project

### Python Side
```bash
pip install -r requirements.txt
python src/main.py


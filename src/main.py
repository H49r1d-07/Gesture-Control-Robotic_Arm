import cv2
import mediapipe as mp
import serial
import serial.tools.list_ports

# -------------------- MediaPipe Initialization --------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# -------------------- Serial Port Detection --------------------
available_ports = [port.device for port in serial.tools.list_ports.comports()]
print("Available COM ports:", available_ports)

if not available_ports:
    print("No Arduino detected. Please connect the board.")
    exit()

selected_port = available_ports[0]

try:
    arduino = serial.Serial(selected_port, 9600)
    print(f"Connected to Arduino on {selected_port}")
except Exception as e:
    print("Serial connection error:", e)
    exit()

# -------------------- Camera Setup --------------------
cap = cv2.VideoCapture(0)
previous_finger_states = None

# -------------------- Main Loop --------------------
while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            finger_states = [0, 0, 0, 0, 0]

            # Thumb detection
            if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
                finger_states[0] = 1

            # Other fingers detection
            tips = [8, 12, 16, 20]
            bases = [5]()

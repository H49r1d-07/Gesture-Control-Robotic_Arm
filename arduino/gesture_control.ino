#include <Servo.h>

Servo thumb;
Servo indexFinger;
Servo middleFinger;
Servo ringFinger;
Servo littleFinger;

String inputData = "";

void setup() {
  Serial.begin(9600);

  thumb.attach(3);
  indexFinger.attach(5);
  middleFinger.attach(6);
  ringFinger.attach(9);
  littleFinger.attach(10);

  Serial.println("Arduino Ready");
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '*') {
      processGesture(inputData);
      inputData = "";
    } else {
      inputData += c;
    }
  }
}

void processGesture(String gesture) {
  if (gesture.length() != 5) return;

  thumb.write(gesture[0] == '1' ? 180 : 0);
  indexFinger.write(gesture[1] == '1' ? 180 : 0);
  middleFinger.write(gesture[2] == '1' ? 180 : 0);
  ringFinger.write(gesture[3] == '1' ? 180 : 0);
  littleFinger.write(gesture[4] == '1' ? 180 : 0);
}

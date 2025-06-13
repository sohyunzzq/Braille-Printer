/////////// 하드웨어에 맞게 핀 번호 수정
int pins[6] = { 2, 3, 4, 5, 6, 7 };

/////////// 이 아래는 수정 X
void setup() {
  Serial.begin(9600);

  for (int i = 0; i < 6; i++) {
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }
}

void loop() {
  if (Serial.available()) {
    char sign = Serial.read();
    Serial.println(sign);

    switch (sign) {
      case '1':
        digitalWrite(pins[0], HIGH);
        break;

      case '2':
        digitalWrite(pins[1], HIGH);
        break;

      case '3':
        digitalWrite(pins[2], HIGH);
        break;

      case '4':
        digitalWrite(pins[3], HIGH);
        break;

      case '5':
        digitalWrite(pins[4], HIGH);
        break;

      case '6':
        digitalWrite(pins[5], HIGH);
        break;

      case '0':
        delay(1000);
        for (int i = 0; i < 6; i++) {
          digitalWrite(pins[i], LOW);
        }
        delay(1000);
        break;
    }
  }
}
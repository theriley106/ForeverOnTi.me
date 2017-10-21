const int buzzerPin = 7;
const int button_pin = 0;

void setup() {
    pinMode(buzzerPin, OUTPUT);
    pinMode(button_pin, INPUT);
}

bool last_button = false;
void loop() {
    bool button = digitalRead(button_pin);
    if (button) {
        digitalWrite(buzzerPin, HIGH);
        delay(100);
        digitalWrite(buzzerPin, LOW);
        }
}
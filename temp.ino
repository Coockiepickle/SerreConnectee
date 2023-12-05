String nom = "Arduino";
int temperaturePin = A0;
String msg;
float temperatureC = 0;

void setup() {
 	Serial.begin(9600);
}

void loop() {
  readSerialPort();

  if (msg == "data") {
    int lecture = analogRead(temperaturePin);

  // Lecture du voltage
    float voltage = lecture * 5.0;
    voltage /= 1024.0;

  // Conversion de la lecture analogique en degrés Celsius
    temperatureC = (voltage - 0.5) * 100;

    sendData();

  delay(1000);
  }
}

void readSerialPort() {
  msg = "";
  if (Serial.available()) {
    delay(10);
    while (Serial.available() > 0) {
      msg += (char)Serial.read();
    }
    Serial.flush();
  }
}

void sendData() {
  Serial.print("x");
 	Serial.print(temperatureC);
}



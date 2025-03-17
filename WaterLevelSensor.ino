// Define the pins
int waterSensorPin = A0; // water level sensor is connected to analog pin A0
int ledPin = 13; // LED is connected to digital pin 13

void setup() {
  // Initialize serial com at 9600 bits per second
  Serial.begin(9600);
  //Initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Read the input on analog pin 0 (A0)
  int sensorValue = analogRead(waterSensorPin);

  // Print out the value you read
  Serial.println(sensorValue);

  //Check if the water level is above our set threshold
  if(sensorValue > 300) {
    digitalWrite(ledPin, HIGH); // Turn on the LED
  } else {
    digitalWrite(ledPin, LOW); // Turn on the LED
  }

  // Wait for a second before taking the next reading
  delay(7000);
}

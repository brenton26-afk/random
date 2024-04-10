// This script is a simple script to test if the Serial port is working 
// There is also a simple script to test the power and output of a board by setting up a simple blinking LED

void setup(){
  // Set up Serial Port
  Serial.begin(9600);
  Serial.print("Hello World");

  //Set up a pin
  // For example, for an LED
  pinMode(10, OUTPUT);
}

// The looping function that will continuously run.
void loop(){
  // Turning on and off an LED.
  digitalWrite(10, HIGH);
  delay(1000);
  digitalWrite(10, LOW);
  delay(1000);
}



// Process of wiring a single LED to an Arduino and breadboard:
// 5v and GND must be wired correctly. Also, there must be a ground wire connecting both GNDs of the breadboard.
// Long side of the LED goes on the inside of the breadboard along with a resistor.
// There is also a wire to the resistor and towards a pin in the Arduino.

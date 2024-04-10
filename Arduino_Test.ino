// This script is a simple script to test if Serial port is working 
// There is also simple scrip to test the power and output of a board by setting up a simpling blinking LED

void setup(){
  // Set up Serial Port
  Serial.begin(9600);
  Serial.print("Hello World");

  //Set up a pin
  // For example, for a LED
  pinMode(10, OUTPUT);
}

// The looping function that will continuously run.
void loop(){
  // Turning on and off a LED.
  digitalWrite(10, HIGH);
  delay(1000);
  digitalWrite(10, LOW);
  delay(1000);
}

/* blink.ino
 * Omkar H. Ramachandran
 * omkar.ramachandran@colorado.edu
 *  
 * Simple Arduino 'hello-world' blink program
 */
#include <avr/io.h>

int analogPin = 0;
int val = 0;
float voltage = 0;
float temperature = 0;
float tempF = 0;

void setup(){
	// Configure pin 7 for output
	Serial.begin(9600);
}

void loop(){
	val = analogRead(analogPin);
	voltage = val*5.0;
	voltage = voltage/1024.;

	temperature = (voltage - 0.5)*100;
	tempF = temperature*9/5.+32;

	if(tempF > 80 || tempF < 60){
		Serial.print(temperature);Serial.println(" Degrees C");
		Serial.print(tempF);Serial.println(" Degrees F");
	}
	delay(1000);
}

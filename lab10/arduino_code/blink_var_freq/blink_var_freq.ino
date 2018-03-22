/* blink_var_freq.ino
 * Omkar H. Ramachandran
 * omkar.ramachandran@colorado.edu
 *  
 * Simple Arduino 'hello-world' blink program
 */
#include <avr/io.h>

int analogPin = 0;
int val = 0;
float voltage = 0;
int f_max=10;
int f_min=1;
int f;
int dtime = 0;

void setup(){
	// Configure pin 7 for output
	pinMode(7, OUTPUT);
	Serial.begin(9600);
}

void loop(){
	val = analogRead(analogPin);
	voltage = 5.0*val/1024.0;
	f = (f_max)*val/1024.0+f_min;	
	dtime = (int) 1000/f;	
	Serial.println(dtime);
	digitalWrite(7, HIGH); // turn LED on
	delay(dtime);
	digitalWrite(7, LOW); //turn LED off
	delay(dtime);
}

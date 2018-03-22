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
int f_max=50;
int f_min=1;
int f;
int dtime = 0;

void setup(){
	// Configure pin 7 for output
	pinMode(11, OUTPUT);
	pinMode(10, OUTPUT);
	pinMode(9, OUTPUT);
	pinMode(8, OUTPUT);
	pinMode(7, OUTPUT);
	pinMode(6, OUTPUT);
	pinMode(5, OUTPUT);
	pinMode(4, OUTPUT);
	pinMode(3, OUTPUT);
	pinMode(2, OUTPUT);

	Serial.begin(9600);
}

void loop(){
	val = analogRead(analogPin);
	voltage = 5.0*val/1024.0;
	f = (f_max)*val/1024.0+f_min;	
	dtime = (int) 1000/f;	
	Serial.println(dtime);
	digitalWrite(11, HIGH);
	delay(dtime/10);	

	digitalWrite(10, HIGH); // turn LED on
	delay(dtime/10);	

	digitalWrite(9, HIGH);
	delay(dtime/10);	

	digitalWrite(8, HIGH);
	delay(dtime/10);	

	digitalWrite(7, HIGH);
	delay(dtime/10);	

	digitalWrite(6, HIGH);
	delay(dtime/10);	

	digitalWrite(5, HIGH);
	delay(dtime/10);	

	digitalWrite(4, HIGH);
	delay(dtime/10);	
	digitalWrite(3, HIGH);
	delay(dtime/10);	

	digitalWrite(2, HIGH);
	delay(dtime/10);	

	delay(dtime);
	digitalWrite(11, LOW);
	digitalWrite(10, LOW); // turn LED on
	digitalWrite(9, LOW);
	digitalWrite(8, LOW);
	digitalWrite(7, LOW);
	digitalWrite(6, LOW);
	digitalWrite(5, LOW);
	digitalWrite(4, LOW);
	digitalWrite(3, LOW);
	digitalWrite(2, LOW);

 //turn LED off
	delay(dtime);
}

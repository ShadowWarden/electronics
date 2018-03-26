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
int f_max=30;
int f_min=1;
int f;
int dtime = 0;
int pin = 0;

void setup(){
	// Configure pin 7 for output
	pinMode(2, OUTPUT);
	pinMode(3, OUTPUT);
	Serial.begin(9600);
}

void loop(){
	val = analogRead(analogPin);
	if(val > 1000){
		pin = 3;
		dtime = 50;
	}else{
		pin = 2;
		dtime = 50;	
	}	
	digitalWrite(pin, HIGH);
	delay(dtime);
	digitalWrite(pin, LOW);
	delay(dtime);
}

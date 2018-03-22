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
unsigned int dtime = 0;
int Nruns = 10;
int i = 0;
int j = 0;

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
	f = (f_max)*val/1024+f_min;	
	dtime = 1000/f;	
	Serial.println(val);
	Serial.println(dtime);
	for(i=2;i<=11;i++){
		digitalWrite(i, HIGH);
		delay(dtime/10);	
		digitalWrite(i, LOW);
		delay(dtime/10);
	}
	//turn LED off
}

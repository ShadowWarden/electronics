/* blink.ino
 * Omkar H. Ramachandran
 * omkar.ramachandran@colorado.edu
 *  
 * Simple Arduino 'hello-world' blink program
 */
#include <avr/io.h>

int i;
int Nruns;

void setup(){
	// Configure pin 7 for output
	pinMode(7, OUTPUT);
	i = 0;
	Nruns = 10;
}

void loop(){
	while(i<Nruns){
		digitalWrite(7, HIGH); // turn LED on
		delay(100);
		digitalWrite(7, LOW); //turn LED off
		delay(100);
		i++;
	}
}

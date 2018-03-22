/* double_blink.ino
 * Omkar H. Ramachandran
 * omkar.ramachandran@colorado.edu
 *  
 * Simple Arduino blink program
 */
#include <avr/io.h>

int i;
int Nruns;

void setup(){
	// Configure pin 7 for output
	pinMode(7, OUTPUT);
	pinMode(4, OUTPUT);
	i = 0;
	Nruns = 10;
}

void loop(){
	while(i<Nruns){
		digitalWrite(4, LOW);
		digitalWrite(7, HIGH); // turn LED on
		delay(1000);
		digitalWrite(4, HIGH);
		digitalWrite(7, LOW); //turn LED off
		delay(1000);
		i++;
	}
	digitalWrite(4,LOW);
	exit(0);
}

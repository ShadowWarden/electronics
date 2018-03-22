/* read.ino
 * Omkar H. Ramachandran
 *
 */

int analogPin = 0;
int val = 0;
float voltage = 0;

void setup(){
	Serial.begin(9600);
}

void loop(){
	val = analogRead(analogPin);
	voltage = 5.0*val/1024.0;
	Serial.println(voltage);
}

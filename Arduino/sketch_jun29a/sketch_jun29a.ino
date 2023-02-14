#include <SPI.h>
#include <Adafruit_PCD8544.h>

int sensorPin = A0; 
Adafruit_PCD8544 display = Adafruit_PCD8544(7, 6, 5, 4, 3);
void setup() {
  // put your setup code here, to run once:
//Serial.begin(9600);

display.begin();
display.setTextSize(1);
display.setContrast(57);
display.clearDisplay();
}

void loop() {
  // put your main code here, to run repeatedly:
int sensorValue = analogRead(sensorPin);
//Serial.println(sensorValue);
display.println(sensorValue);
display.print((sensorValue/1023.0)*100);
display.println("%"); 

//long adconvert=(sensorValue-0.82)*(1023-167.77)/(5-0.82)+167.77;
//long psia = (adconvert-167.77)*(58.0152-7.2519)/(1023-167.77)+7.2519;
//long psig = psia-14.7;
//display.print(psig);
//display.println(" psi");




display.display();
delay(10);
display.clearDisplay();
}

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();
RCSwitch recSwitch = RCSwitch();
void setup() {

  Serial.begin(9600);
  
  // Transmitter is connected to Arduino Pin #10  
  mySwitch.enableTransmit(10);
  recSwitch.enableReceive(0);
  // Optional set protocol (default is 1, will work for most outlets)
  // mySwitch.setProtocol(2);

  // Optional set pulse length.
  // mySwitch.setPulseLength(320);
  
  // Optional set number of transmission repetitions.
  // mySwitch.setRepeatTransmit(15);
  
}

void loop() {

  /* See Example: TypeA_WithDIPSwitches */
  mySwitch.switchOn("11111", "00010");
  rec(recSwitch);
  //delay(1000);
  mySwitch.switchOff("11111", "00010");
  rec(recSwitch);
  //delay(1000);

  /* Same switch as above, but using decimal code */
  mySwitch.send(5393, 24);
  rec(recSwitch);
  //delay(1000);  
  mySwitch.send(5396, 24);
  rec(recSwitch);
  //delay(1000);  

  /* Same switch as above, but using binary code */
  mySwitch.send("000000000001010100010001");
  rec(recSwitch);
  //delay(1000);  
  mySwitch.send("000000000001010100010100");
  rec(recSwitch);
  //delay(1000);

  /* Same switch as above, but tri-state code */ 
  mySwitch.sendTriState("00000FFF0F0F");
  rec(recSwitch);
  //delay(1000);  
  mySwitch.sendTriState("00000FFF0FF0");
  rec(recSwitch);
  //delay(1000);
  
  //delay(20000);
} 

void rec(RCSwitch mySwitch) {
  if (mySwitch.available()) {
    
    int value = mySwitch.getReceivedValue();
    //Serial.println(value);
    if (value == 0) {
      Serial.print("Unknown encoding");
    } else {
      Serial.print("Received ");
      Serial.print( mySwitch.getReceivedValue() );
      Serial.print(" / ");
      Serial.print( mySwitch.getReceivedBitlength() );
      Serial.print("bit ");
      Serial.print("Protocol: ");
      Serial.println( mySwitch.getReceivedProtocol() );
    }

    mySwitch.resetAvailable();
  }
}

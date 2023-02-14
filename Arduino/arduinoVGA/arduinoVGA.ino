/*************************************************************************
 * 
 * VGA output with Arduino (white and black colors).
 * This is a free software with NO WARRANTY.
 * https://simple-circuit.com/
 *
 ************************************************************************/
 
#include <Adafruit_GFX.h>  // include Adafruit graphics library
#include "VGA.h"           // include VGA library

char art[5][67]={
"H   H EEEEE L     L      OOO       W   W  OOO  RRRR  L     DDDD  !!",
"H   H E     L     L     O   O      W W W O   O R   R L     D   D !!",
"HHHHH EEEEE L     L     O   O      W W W O   O RRRR  L     D   D !!",
"H   H E     L     L     O   O  ,,   W W  O   O R   R L     D   D   ",
"H   H EEEEE LLLLL LLLLL  OOO  ,,    W W   OOO  R   R LLLLL DDDD  !!"
};
 
// initialize the VGA library
VGA display = VGA();
 
void setup(void) {
  // initialize the VGA display
  display.begin();
 
  display.delay(5000);     // wait 5 seconds
  display.clearDisplay();  // clear the screen buffer
 
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 0);
  display.println("Hello, world!");
  display.setTextColor(BLACK, WHITE);
  display.println(3.141592);
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.print("0x");
  display.println(0xDEADBEEF, HEX);
 
  display.setCursor(0, 40);
  display.setTextSize(1);
  display.print("Arduino VGA Exampl");
  
  /*display.clearDisplay();
  /*while(1)
  {
    //display.clearDisplay();
    for(int j=0;j<40;j++)
    {
      display.clearDisplay();
      for(int i=0;i<30;i++)
      {
        //display.clearDisplay();
        //display.setCursor(i, 40);
        //display.setTextSize(1);
        //display.print("A");
        display.drawPixel(i, j, 1);
        //display.delay(5);
      }
      display.delay(5);
    }
    //break;
  }*/

  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 0);
  for(int i=0;i<5;i++)
  {
    //display.setCursor(0, i);
    display.println(art[i]);
  }

}
 
void loop() {
  ;
}
 
// end of code.

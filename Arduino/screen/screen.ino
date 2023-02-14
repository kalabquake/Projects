#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>

// Declare LCD object for software SPI
// Adafruit_PCD8544(CLK,DIN,D/C,CE,RST);
Adafruit_PCD8544 display = Adafruit_PCD8544(13, 11, 9, 10, 8);

int rotatetext = 1;

int snakePos[80][2]={{5,5},{4,4},{3,3},{2,2},{1,1},{0,0}};
int size=5;
int dir[2]={0,1};

void moveSnake()
{
  int part=0;
  for(part=size-1;part>0;part--)
  {
    snakePos[part][0]=snakePos[part-1][0];
    snakePos[part][1]=snakePos[part-1][1];
  }
  snakePos[0][0]+=dir[0];
  snakePos[0][1]+=dir[1];
}

void showSnake()
{
  for(int i=0;i<size;i++)
  {
    display.drawRect(snakePos[i][0], snakePos[i][1], 1, 1, BLACK);
  }
    display.display();
}

void setup()   {
  Serial.begin(9600);

  //Initialize Display
  display.begin();

  /*
  // you can change the contrast around to adapt the display for the best viewing!
  display.setContrast(57);

  // Clear the buffer.
  display.clearDisplay();

  // Display Text
  display.setTextSize(1);
  display.setTextColor(BLACK);
  display.setCursor(0,0);
  display.println("Hello world!");
  display.display();
  delay(2000);
  display.clearDisplay();


  // Display Inverted Text
  display.setTextColor(WHITE, BLACK); // 'inverted' text
  display.setCursor(0,0);
  display.println("Hello world!");
  display.display();
  delay(2000);
  display.clearDisplay();

  // Scaling Font Size
  display.setTextColor(BLACK);
  display.setCursor(0,0);
  display.setTextSize(2);
  display.println("Hello!");
  display.display();
  delay(2000);
  display.clearDisplay();

  // Display Numbers
  display.setTextSize(1);
  display.setCursor(0,0);
  display.println(123456789);
  display.display();
  delay(2000);
  display.clearDisplay();

  // Specifying Base For Numbers
  display.setCursor(0,0);
  display.print("0x"); display.print(0xFF, HEX); 
  display.print("(HEX) = ");
  display.print(0xFF, DEC);
  display.println("(DEC)"); 
  display.display();
  delay(2000);
  display.clearDisplay();*/

/*display.clearDisplay();
  // Display ASCII Characters
  display.setCursor(0,0);
  display.setTextSize(5);
  display.write(97);
  display.display();
  delay(2000);
  display.clearDisplay();
  */

  // Text Rotation
  /*while(1)
  {
  display.clearDisplay();
  display.setRotation(rotatetext);  // rotate 90 degrees counter clockwise, can also use values of 2 and 3 to go further.
  display.setTextSize(1);
  display.setTextColor(BLACK);
  display.setCursor(0,0);
  display.println("Text Rotation");
  display.display();
  //delay(1000);
  display.clearDisplay();
  rotatetext++;
  }*/
  /*while(1){
  int pos=0;
  display.clearDisplay();
    for(int i=0;i<20;i++)
    {
    //display.clearDisplay();
    display.drawRect(i, 0, 1, 1, BLACK);
    display.display();
    //delay(2000);
    }
    for(int i=0;i<20;i++)
    {
    //display.clearDisplay();
    display.drawRect(20, i, 1, 1, BLACK);
    display.display();
    //delay(2000);
    }
    for(int i=20;i>0;i--)
    {
    //display.clearDisplay();
    display.drawRect(i, 20, 1, 1, BLACK);
    display.display();
    //delay(2000);
    }
    for(int i=20;i>0;i--)
    {
    //display.clearDisplay();
    display.drawRect(0, i, 1, 1, BLACK);
    display.display();
    //delay(2000);
    }
    delay(2000);
  }*/
  display.clearDisplay();
  while(1)
  {
    moveSnake();
    showSnake();
    delay(100);
    display.clearDisplay();
    if(snakePos[0][0]>60 || snakePos[0][1]>60)
      break;
  }
}

void loop() {}

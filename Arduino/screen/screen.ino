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

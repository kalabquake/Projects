#include <FastLED.h>

FASTLED_USING_NAMESPACE

// FastLED "100-lines-of-code" demo reel, showing just a few 
// of the kinds of animation patterns you can quickly and easily 
// compose using FastLED.  
//
// This example also shows one easy way to define multiple 
// animations patterns and have them automatically rotate.
//
// -Mark Kriegsman, December 2014


#define DATA_PIN    3
//#define CLK_PIN   4
#define LED_TYPE    WS2811
#define COLOR_ORDER GRB
#define NUM_LEDS    109
CRGB leds[NUM_LEDS];

int toggleBTN = 5;
bool showLED = true;

#define BRIGHTNESS          255
#define FRAMES_PER_SECOND   120

void setup() {
  delay(3000); // 3 second delay for recovery

  pinMode(toggleBTN,INPUT_PULLUP);
  // tell FastLED about the LED strip configuration
  FastLED.addLeds<LED_TYPE,DATA_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  //FastLED.addLeds<LED_TYPE,DATA_PIN,CLK_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);

  // set master brightness control
  FastLED.setBrightness(BRIGHTNESS);
  Serial.begin(9600);
}


// List of patterns to cycle through.  Each is defined as a separate function below.
typedef void (*SimplePatternList[])();
SimplePatternList gPatterns = { rainbow, rainbowWithGlitter,confetti, sinelon, juggle, bpm, turnOffLeds};

uint8_t gCurrentPatternNumber = 0; // Index number of which pattern is current
uint8_t gHue = 0; // rotating "base color" used by many of the patterns

int count=0;
#define ARRAY_SIZE(A) (sizeof(A) / sizeof((A)[0]))


void loop()
{
  // Call the current pattern function once, updating the 'leds' array
  gPatterns[gCurrentPatternNumber]();

  // send the 'leds' array out to the actual LED strip
  FastLED.show();  
  // insert a delay to keep the framerate modest
  FastLED.delay(1000/FRAMES_PER_SECOND); 

  // do some periodic updates
  
  if(showLED!=digitalRead(toggleBTN))
  {
    showLED=!showLED;
    count+=1;
    if(count%2==0)//button will flip twice, once per press and once per release, so this should run after one full button press, or on button release
    {
      gCurrentPatternNumber=(gCurrentPatternNumber+1)%ARRAY_SIZE(gPatterns);//cycle through patterns
      Serial.println(gCurrentPatternNumber);
      switch(gCurrentPatternNumber)
      {
        case 0:
          Serial.println("Rainbow");
          break;
        case 1:
          Serial.println("Rainbow with glitter");
          break;
        case 2:
          Serial.println("Confetti");
          break;
        case 3:
          Serial.println("Sinelon");
          break;
        case 4:
          Serial.println("Juggle");
          break;
        case 5:
          Serial.println("BPM");
          break;
        case 6:
          Serial.println("Turn LEDs off");
          break;
        case 7:
          Serial.println("Rainbow");
        default:
          Serial.println("Unexpected gCurrentPatternNumber");
      }
    }
  }
  EVERY_N_MILLISECONDS( 20 ) { gHue++; } // slowly cycle the "base color" through the rainbow
  //EVERY_N_SECONDS( 10 ) { nextPattern(); } // change patterns periodically
}



void nextPattern()
{
  // add one to the current pattern number, and wrap around at the end
  gCurrentPatternNumber = (gCurrentPatternNumber + 1) % ARRAY_SIZE( gPatterns);
}
bool red=true;
long a=millis();
void rainbow() 
{/*
  // FastLED's built-in rainbow generator
  fill_rainbow( leds, NUM_LEDS, gHue, 255);
  
}

void cops1()
{
  //Serial.println();
  
  if(millis()-a>300)
  {
    red=!red;
    a=millis();
  }
  fadeToBlackBy( leds, NUM_LEDS, 4);
  for(int i=0; i<ARRAY_SIZE(leds);i++)
  {
    if(red)
      //leds[i] = CHSV(0, 255, 255);
      {
        if(i%2==0)
          leds[i] = CRGB::Red;
        else
          leds[i] = CRGB::Black;
      }
    else
      //leds[i] = CHSV(170, 255, 255);
      {
        if(i%2==1)
          leds[i] = CRGB::Blue;
        else
          leds[i] = CRGB::Black;
      }
  }
  
}

void cops2()
{*/
  //Serial.println();
  
  if(millis()-a>300)
  {
    red=!red;
    a=millis();
  }
  fadeToBlackBy( leds, NUM_LEDS, 4);
  for(int i=0; i<ARRAY_SIZE(leds);i++)
  {
    if(red)
      //leds[i] = CHSV(0, 255, 255);
      {
        if(i>ARRAY_SIZE(leds)/2)
          leds[i] = CRGB::Red;
        else
          leds[i] = CRGB::Black;
      }
    else
      //leds[i] = CHSV(170, 255, 255);
      {
        if(i<(ARRAY_SIZE(leds)/2)+1)
          leds[i] = CRGB::Blue;
        else
          leds[i] = CRGB::Black;
      }
  }
  
}

void seizure()
{
  // FastLED's built-in rainbow generator
  //fill_rainbow( leds, NUM_LEDS, gHue, 1);
  //fadeToBlackBy( leds, NUM_LEDS, 4);
  for(int i=0; i<ARRAY_SIZE(leds);i++)
  {
    //Serial.println(gHue);
    if(gHue<42)
      gHue=42;
    else if(gHue>192)
      gHue=0;
    //Serial.println((int)((((float)i/109.0))*255));
    leds[i] = CHSV(gHue, 255, 255);
    //(((int)((((float)i/109.0))*255))+0)
    //random16(170)+43
  }
  gHue+=10;
}

void rainbowWithGlitter() 
{
  // built-in FastLED rainbow, plus some random sparkly glitter
  rainbow();
  addGlitter(80);
}

void turnOffLeds() 
{  
  for(int i =0; i<ARRAY_SIZE(leds);i++)
    fadeToBlackBy( leds, NUM_LEDS, 1);
}

void addGlitter( fract8 chanceOfGlitter) 
{
  if( random8() < chanceOfGlitter) {
    leds[ random16(NUM_LEDS) ] += CRGB::White;
  }
}

/*void confetti() 
{
  // random colored speckles that blink in and fade smoothly
  fadeToBlackBy( leds, NUM_LEDS, 10);
  int pos = random16(NUM_LEDS);
  leds[pos] += CHSV( gHue + random8(64), 200, 255);
}*/

void confetti() 
{
  // random colored speckles that blink in and fade smoothly
  fadeToBlackBy( leds, NUM_LEDS, 4);
  int pos = random16(NUM_LEDS);
  
  int hue=random16(3);
  Serial.println(hue);
  hue*=85;
  leds[pos] += CHSV( hue, 200, 255);
}

void sinelon()
{
  // a colored dot sweeping back and forth, with fading trails
  fadeToBlackBy( leds, NUM_LEDS, 20);
  int pos = beatsin16( 13, 0, NUM_LEDS-1 );
  Serial.println(gHue);
  leds[pos] += CHSV( 0, 255, 192);
}

void bpm()
{
  // colored stripes pulsing at a defined Beats-Per-Minute (BPM)
  uint8_t BeatsPerMinute = 62;
  CRGBPalette16 palette = PartyColors_p;
  uint8_t beat = beatsin8( BeatsPerMinute, 64, 255);
  for( int i = 0; i < NUM_LEDS; i++) { //9948
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void juggle() {
  // eight colored dots, weaving in and out of sync with each other
  fadeToBlackBy( leds, NUM_LEDS, 20);
  uint8_t dothue = 0;
  for( int i = 0; i < 8; i++) {
    leds[beatsin16( i+7, 0, NUM_LEDS-1 )] |= CHSV(dothue, 200, 255);
    dothue += 32;
  }
}

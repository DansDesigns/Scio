/* ESP32 Neopixel working 14/01/25
   Customised for embedding in Scio (Scicorder Pro)with C3
   use lolin c3 pico board
   To DO:
     add serial communications
     add commands to change colours
     create colour sequence to match sensor page

     INCORPORATE SLEEP FUNCTION:
      - SEND SLEEP/WAKE COMMAND FROM PYGAME:
        - SLEEP/WAKE ESP32 - EXTRA GPIO?
                           - WAKE OVER USB?
                           - POWER PINS ON NANOPI NEO TURN OFF WHEN ASLEEP - IF SO ABOVE IS NOT NEEDED, JUST CONFIG COMMANDS
*/

#include <Adafruit_NeoPixel.h>


#define PIN 10 // NeoPixel Data Pin
#define NUMPIXELS 2 // no. Neopixels attached
#define DELAYVAL 500 // Time (in milliseconds) to pause between pixels


Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);


void setup()
{
  Serial.begin(9600);
  pixels.begin(); // INITIALIZE NeoPixels
}


void loop()
{
  Serial.println("new loop starting");
  pixels.clear(); // Set all pixel colors to 'off'

  // The first NeoPixel in a strand is #0, second is 1, all the way up
  for (int i = 0; i < NUMPIXELS; i++) // For each pixel...
  {
    // pixels.Color() takes RGB values, from 0,0,0 up to 255,255,255
    pixels.setPixelColor(i, pixels.Color(0, 15, 15));
    pixels.show();   // Send the updated pixel colors to the hardware.
    delay(DELAYVAL); // Pause before next pass through loop
  }

  pixels.setPixelColor(0, pixels.Color(20, 0, 15));
  pixels.show();   // Send the updated pixel colors to the hardware.
  delay(1000);
}

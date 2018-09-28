#include <FastLED.h>
#include <bitswap.h>
#include <chipsets.h>
#include <color.h>
#include <colorpalettes.h>
#include <colorutils.h>
#include <controller.h>
#include <cpp_compat.h>
#include <dmx.h>
#include <fastled_config.h>
#include <fastled_delay.h>
#include <fastled_progmem.h>
#include <fastpin.h>
#include <fastspi.h>
#include <fastspi_bitbang.h>
#include <fastspi_dma.h>
#include <fastspi_nop.h>
#include <fastspi_ref.h>
#include <fastspi_types.h>
#include <hsv2rgb.h>
#include <led_sysdefs.h>
#include <lib8tion.h>
#include <noise.h>
#include <pixelset.h>
#include <pixeltypes.h>
#include <platforms.h>
#include <power_mgt.h>
#include "FastLED.h"
#include <avr/pgmspace.h>
#define NUM_LEDS 15


int rpm = 300;
long timeold;
long timedelta;
long time_per_rotation = 200;
float segment_size = 0.25;
int sensorPin = A0; // select the input pin for LDR
int sensorValue = 0; // variable to store the value coming from the sensor


CRGB leds[NUM_LEDS];
void setup() { 
  Serial.begin(9600); //sets serial port for communication
  FastLED.addLeds<NEOPIXEL, 6>(leds, NUM_LEDS);
  timeold = millis();
}


void loop() {
    sensorValue = analogRead(sensorPin);
    time_per_rotation = sensorValue / 2;
//    time_per_rotation = 124; // This was a good value with dremel speed 6
    Serial.println(time_per_rotation);
    timedelta = millis() - timeold;

    for(int i=0; i < 7; i++){
      leds[0 + i] = CRGB::Red; FastLED.show();
    }
    delay(time_per_rotation * segment_size);
    for(int i=0; i < 7; i++){
      leds[0 + i] = CRGB::Blue; FastLED.show();
    }
    delay(time_per_rotation * segment_size);
    for(int i=0; i < 7; i++){
      leds[0 + i] = CRGB::Green; FastLED.show();
    }
    delay(time_per_rotation * segment_size);
    for(int i=0; i < 7; i++){
      leds[0 + i] = CRGB::White; FastLED.show();
    }
    delay(time_per_rotation * segment_size);
}

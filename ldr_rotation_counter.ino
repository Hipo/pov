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
#define NUM_LEDS 15
int sensorPin = A0; // select the input pin for LDR
int sensorValue = 0; // variable to store the value coming from the sensor

bool detect = false;
int ldr_threshold = 600;
int revolutions = 0;
long timeold;
long rpm;
long minute = 60000;

CRGB leds[NUM_LEDS];
void setup() { 
  Serial.begin(9600); //sets serial port for communication
  FastLED.addLeds<NEOPIXEL, 6>(leds, NUM_LEDS);
  timeold = millis();
}

void loop() {
  leds[14] = CRGB::White; FastLED.show();
  sensorValue = analogRead(sensorPin); // read the value from the sensor
  if(sensorValue > ldr_threshold && !detect){
    detect = true;
    revolutions += 1;
    rpm = minute / (millis() - timeold);
    timeold = millis();
    Serial.print(sensorValue);
    Serial.print(" ");
    Serial.print(rpm);
    Serial.print(" ");
    Serial.println(revolutions);
  }
  if (sensorValue < ldr_threshold){
    detect = false;
  }
}

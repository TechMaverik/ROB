#include <Wire.h>
#include <Arduino.h>
#include <Adafruit_PWMServoDriver.h>
#include "robWiFi.h"
#include "robMotionPlanner.h"
#include "robDisplay.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1

bool status;
int led=23;
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();


void setup()
{
  Serial.begin(9600);
  Serial.println("[ *** ROB FIRMWARE v BETA ***");
  pinMode(led,OUTPUT);
  pwm.begin();
  pwm.setPWMFreq(60);
  connect_to_wifi(led);
  homePosition(pwm);
  status= homePosition(pwm);
}

void loop()
{  
  
}

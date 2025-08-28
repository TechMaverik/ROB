#include <Wire.h>
#include <Arduino.h>
#include <Adafruit_PWMServoDriver.h>
#include "robWiFi.h"
#include "robMotionPlanner.h"

bool status;
int led=23;
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

void setup()
{
  Serial.begin(115200);
  pinMode(led,OUTPUT);
  pwm.begin();
  pwm.setPWMFreq(60);
}

void loop()
{
  connect_to_wifi(led);
  status= homePosition(pwm);
}

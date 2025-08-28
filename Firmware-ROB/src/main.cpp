#include <Wire.h>
#include <Arduino.h>
#include <Adafruit_PWMServoDriver.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "robWiFi.h"
#include "robMotionPlanner.h"
#include "robDisplay.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1

bool status;
int led=23;
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup()
{
  Serial.begin(115200);
  pinMode(led,OUTPUT);
  pwm.begin();
  pwm.setPWMFreq(60);
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { 
    Serial.println(F("Rob Display allocation FAILED"));
    while (true); 
  }
}

void loop()
{  
  showMessage("ROB-ROS2",2,0,0,display);
  showMessage("Firmware 1.0 Beta",2,1,0,display);
  connect_to_wifi(led,display);
  clearDisplay(display);
  showMessage("ROB-ROS2",2,0,0,display);
  showMessage("IP:",2,1,0,display);
  showMessage("192.168.x.x",2,1,4,display);
  homePosition(pwm);
  status= homePosition(pwm);
}

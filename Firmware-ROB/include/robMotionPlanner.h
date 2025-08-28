#include <Adafruit_PWMServoDriver.h>
#pragma
int angleToPWM(int);
void motionPlanner(Adafruit_PWMServoDriver,int,int,int,int,int);
bool homePosition(Adafruit_PWMServoDriver);
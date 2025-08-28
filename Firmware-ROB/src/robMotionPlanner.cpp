#include <Wire.h>
#include <Arduino.h>
#include <Adafruit_PWMServoDriver.h>
#include "robMotionPlanner.h"


#define SERVO_MIN_ANGLE 0
#define SERVO_MAX_ANGLE 180
#define SERVO_MIN_PULSE 500   
#define SERVO_MAX_PULSE 2500  

int angleToPWM(int angle)
{
    angle = constrain(angle, SERVO_MIN_ANGLE, SERVO_MAX_ANGLE);
    int pulse_us = map(angle, SERVO_MIN_ANGLE, SERVO_MAX_ANGLE, SERVO_MIN_PULSE, SERVO_MAX_PULSE);
    int pwm_val = (int)((pulse_us * 4096.0) / 20000.0); 
    return pwm_val;
}

bool homePosition(Adafruit_PWMServoDriver pwm)
{
    int baseRotationJoint=90;
    int shoulderJoint=90;
    int elbowJoint=90;
    int wristJoint=90;
    int endEffector=90;
    motionPlanner(pwm,baseRotationJoint,shoulderJoint,elbowJoint,wristJoint,endEffector);
    return true;
}

void motionPlanner(Adafruit_PWMServoDriver pwm,int baseRotationJoint,int shoulderJoint, int elbowJoint,int wristJoint,int endEffector)
{
    int baseRotationJointPWM=angleToPWM(baseRotationJoint);
    int shoulderJointPWM=angleToPWM(shoulderJoint);
    int elbowJointPWM=angleToPWM(elbowJoint);
    int wristJointPWM=angleToPWM(wristJoint);
    int endEffectorPWM=angleToPWM(endEffector);

    pwm.setPWM(0, 0, baseRotationJointPWM);
    pwm.setPWM(1, 0, shoulderJointPWM);
    pwm.setPWM(2, 0, elbowJointPWM);
    pwm.setPWM(3, 0, wristJointPWM);
    pwm.setPWM(4, 0, endEffectorPWM);

}
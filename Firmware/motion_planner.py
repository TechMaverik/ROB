from machine import I2C, Pin
from drivers.pca9685 import PCA9685
from drivers.servo import Servos
import configurations
import time


class MotionPlanner:

    def __init__(self):
        self.i2c = I2C(0, scl=Pin(22), sda=Pin(21))
        self.pca = PCA9685(self.i2c)
        self.pca.freq(50)
        self.servos = Servos(self.i2c)
        self.channel_1 = configurations.CHANNEL_1
        self.channel_2 = configurations.CHANNEL_2
        self.channel_3 = configurations.CHANNEL_3
        self.channel_4 = configurations.CHANNEL_4
        self.channel_5 = configurations.CHANNEL_5
        self.default_angle = configurations.DEFAULT_ANGLE
        self.speed = configurations.SPEED

    def set_default_position(self):
        self.servos.position(index=self.channel_1, degrees=self.default_angle)
        time.sleep(1)
        self.servos.position(index=self.channel_2, degrees=self.default_angle)
        time.sleep(1)
        self.servos.position(index=self.channel_3, degrees=self.default_angle)
        time.sleep(1)
        self.servos.position(index=self.channel_4, degrees=self.default_angle)
        time.sleep(1)
        self.servos.position(index=self.channel_5, degrees=self.default_angle)
        time.sleep(1)

    
    def sweep(self, channel):               
        for angle in range(self.default_angle, 181, self.speed):
            self.servos.position(index=channel, degrees=angle)
            print(angle)
            time.sleep(0.02)
        for angle in range(181, self.default_angle, -self.speed):
            self.servos.position(index=channel, degrees=angle)
            print(angle)
            time.sleep(0.02)
        for angle in range(self.default_angle, 0, -self.speed):
            self.servos.position(index=channel, degrees=angle)
            print(angle)
            time.sleep(0.02)
        for angle in range(0, self.default_angle ,self.speed):
            self.servos.position(index=channel, degrees=angle)
            print(angle)
            time.sleep(0.02)



# MotionPlanner().set_default_position()
# time.sleep(1)
# MotionPlanner().sweep()

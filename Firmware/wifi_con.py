import time
import network
import configurations
from machine import Pin, I2C
import ssd1306


class WifiCon:
    def __init__(self):
        self.i2c = I2C(0, scl=Pin(22), sda=Pin(21))
        self.oled = ssd1306.SSD1306_I2C(128, 64, self.i2c)

    def connect(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        led = Pin(23, Pin.OUT)
        ssid = configurations.SSID
        password = configurations.PSW
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            self.oled.fill(0)
            self.oled.text("ROB Ver 1.0", 0, 0)
            self.oled.text("Powered by", 0, 10)
            self.oled.text("HLEngine3", 0, 20)
            self.oled.text("Connecting...", 0, 30)
            self.oled.show()
            print("Connecting...")
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(1)
        print("ROB Connected")
        print("Network config:", wlan.ifconfig())
        self.oled.fill(0)
        self.oled.text("ROB  Ver 1.0", 0, 0)
        self.oled.text("IP: " + wlan.ifconfig()[0], 0, 10)
        self.oled.text("SSID: " + ssid, 0, 20)
        self.oled.text("Designed in:", 0, 30)
        self.oled.text("AI and D&T LAB:", 0, 40)
        self.oled.text("DPSIndirapuram", 0, 50)
        self.oled.show()

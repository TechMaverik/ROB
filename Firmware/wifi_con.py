import time
import network
import configurations
from machine import Pin


class WifiCon:

    def connect(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        led = Pin(23, Pin.OUT)
        ssid = configurations.SSID
        password = configurations.PSW
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            print("Connecting...")
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(1)
        print("Connected to WiFi!")
        print("Network config:", wlan.ifconfig())

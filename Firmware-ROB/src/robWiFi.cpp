#include <WiFi.h>
#include <Arduino.h>
#include <Adafruit_SSD1306.h>
#include "robDisplay.h"

void connect_to_wifi(int led, Adafruit_SSD1306 display)
{
    const char* ssid = "YOUR_SSID";
    const char* password = "YOUR_PASSWORD";
    WiFi.begin(ssid, password);
    showMessage("Connecting .....",3,0,0,display);
    while (WiFi.status() != WL_CONNECTED) {    
        digitalWrite(led,HIGH);
        delay(500);
        digitalWrite(led,LOW);
        delay(500);
  }
}
#include <WiFi.h>
#include <Arduino.h>

void connect_to_wifi(int led)
{
    const char* ssid = "YOUR_SSID";
    const char* password = "YOUR_PASSWORD";
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {    
        digitalWrite(led,HIGH);
        delay(500);
        digitalWrite(led,LOW);
        delay(500);
  }
}
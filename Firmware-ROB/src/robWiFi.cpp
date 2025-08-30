#include <WiFi.h>
#include <Arduino.h>

void connect_to_wifi(int led)
{
    const char* ssid = "Ai Lab";
    const char* password = "Welc0me@123";
    WiFi.begin(ssid, password);
    Serial.println("Connecting ...");
  
    while (WiFi.status() != WL_CONNECTED) {    
        Serial.print(".");
        digitalWrite(led,HIGH);
        delay(500);
        digitalWrite(led,LOW);
        delay(500);
  }
  digitalWrite(led,HIGH);
}
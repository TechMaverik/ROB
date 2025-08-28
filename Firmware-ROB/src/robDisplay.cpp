#include <Arduino.h>
#include <Adafruit_SSD1306.h>
#include "robDisplay.h"


bool showMessage(String message, int size,int cursor_x,int cursor_y,Adafruit_SSD1306 display)
{
    
    display.setTextSize(size);
    display.setTextColor(SSD1306_WHITE);
    display.setCursor(cursor_x,cursor_y);
    display.println(message);
    display.display();  

}

void clearDisplay(Adafruit_SSD1306 display)
{
    display.clearDisplay();
}
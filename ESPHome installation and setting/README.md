# ESPHome installation and setting
> ESPHome is a system to control your ESP8266/ESP32 by simple yet powerful configuration files and control them remotely through Home Automation systems.
![](https://esphome.io/_images/logo-text.svg)
## Hardware
  1. There are many kinds of hardware support ESPHome: `ESP8266`, `ESP8266 NodeMCU`, `ESP32` and `ESP32 NodeMCU`. And there are also many versions, so be careful the differences of serial port and pin point.
  2. Here I use the `ESP8266 NodeMCUv3`, a latest version with a `CH340` serial port. And I list the reasons why I chose this one:
      * It is natively supported by the integration of `HASS.io`, it can be managed very easily.
      * It has enough GPIOs to connect and test, even provide an `ADC pin`, better than `Raspberry Pi`.
      * After connected to Wi-Fi, it can be flashed and uploaded OTA(over-the-air), no wire needed.
      * It is cheap enough, about 5$.
      * The `.yaml` file is easy to configure. Moreover, you could use `ESPeasy` firmware to help you. ([ESPeasy](https://www.letscontrolit.com/wiki/index.php/ESPEasy))
![]()
## ESP8266 connect to Wi-Fi(First time): Arduino IDE way
  1. Install `Arduino IDE`, it can be found at Microsoft Store. ([Link](https://www.arduino.cc/en/Main/software))
![](https://www.arduino.cc/en/pub/skins/arduinoWide/img/ArduinoAPP-01.svg)
  2. Install serial port driver, if use `CH34X` serial port you can find drivers [here](http://www.wch-ic.com/download/ch341ser_exe.html).
  3. Enter http://arduino.esp8266.com/stable/package_esp8266com_index.json into Additional Board Manager URLs field.
  4. Search and install your platform ESP8266 or ESP32.
  ![](https://github.com/Gry1995/Iot-Project/blob/master/ESPHome%20installation%20and%20setting/arduino.PNG)
  5. Connect board to your PC.
  6. Setting Wi-Fi configuration, edit yor `ssid`, `password` and `Braud Rate`.
  ```python
  #include "ESP8266WiFi.h"

    const char* ssid = "ssid";   //your ssid
    const char* password = "password";   //your pw

    void setup(void)
    { 
      Serial.begin(9600);      //Baud rate you are using
      
      WiFi.begin(ssid, password);

      while (WiFi.status() != WL_CONNECTED) {
         delay(500);
         Serial.print(".");
      }
      //print a new line, then print WiFi connected and the IP address
      Serial.println("");
      Serial.println("WiFi connected");
      // Print the IP address
      Serial.println(WiFi.localIP());

    }
    void loop() {

    }
  ```
## ESP8266 connect to Wi-Fi(First time): HASS.io way

# ESPHome installation and setting
> ESPHome is a system to control your ESP8266/ESP32 by simple yet powerful configuration files and control them remotely through Home Automation systems.
![](https://esphome.io/_images/logo-text.svg)
## Hardware
  1. There are many kinds of hardware support ESPHome: `ESP8266`, `ESP8266 NodeMCU`, `ESP32` and `ESP32 NodeMCU`. And there are also many versions, so be careful the differences of serial port and pin point.
  2. Here I use the `ESP8266 NodeMCUv3`, a latest version with a `CH340` serial port. And I list the reasons why I chose this one:
      * The IoT library of ESPHome is huge, and it is easy to customize and use.
      * It is natively supported by the integration of `HASS.io`, it can be managed very easily.
      * It has enough GPIOs to connect and test, even provide an `ADC pin`, better than `Raspberry Pi`.
      * After connected to Wi-Fi, it can be flashed and uploaded OTA(over-the-air), no wire needed.
      * It is cheap enough, about 5$.
      * The `.yaml` file is easy to configure. Moreover, you could use `ESPeasy` firmware to help you. ([ESPeasy](https://www.letscontrolit.com/wiki/index.php/ESPEasy))
![](https://github.com/Gry1995/Iot-Project/blob/master/ESPHome%20installation%20and%20setting/IMG_3087.jpg)
## ESP8266 connect to Wi-Fi(First time): Arduino IDE way
  1. Install `Arduino IDE`, it can be found at Microsoft Store. ([Link](https://www.arduino.cc/en/Main/software))
![](https://www.arduino.cc/en/pub/skins/arduinoWide/img/ArduinoAPP-01.svg)
  2. Install serial port driver, if use `CH34X` serial port you can find drivers [here](http://www.wch-ic.com/download/ch341ser_exe.html).
  3. Enter http://arduino.esp8266.com/stable/package_esp8266com_index.json into Additional Board Manager URLs field.
  4. Search and install your platform ESP8266 or ESP32.
  ![](https://github.com/Gry1995/Iot-Project/blob/master/ESPHome%20installation%20and%20setting/arduino.PNG)
  5. Connect board to your PC.
  6. Set Wi-Fi configuration, edit yor `ssid`, `password` and `Braud Rate`.
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
  1. Search and install `ESPhome` at your HASS Addon store, or use docker to install.
  ![](https://github.com/Gry1995/Iot-Project/blob/master/ESPHome%20installation%20and%20setting/addonstore.PNG)
  2. `Click plus` -> `Creat new node` -> `Name your node` -> `Select your devices` -> 'Enter your ssid/password'.
  ![](https://github.com/Gry1995/Iot-Project/blob/master/ESPHome%20installation%20and%20setting/creat%20node.PNG)
  3. You also can edit the `.yaml` file after wizard.
  4. Check, validate and compile the file to your PC.
  ![](https://github.com/Gry1995/Iot-Project/blob/master/ESPHome%20installation%20and%20setting/compile.PNG)
  5. Install serial port driver, if use `CH34X` serial port you can find drivers [here](http://www.wch-ic.com/download/ch341ser_exe.html).
  6. Install [ESPFlasher](https://github.com/esphome/esphome-flasher/releases), it can add your setting file into the board. 
  7. Now the ESP8266 will connect to the Wi-Fi, it can be upload over the air.
  
## Connect your ESP board to HASS.io

  Example: use ESP8266 to test signal strength.
  1. Edit `test.yaml` file.
  ```python
  sensor:
    - platform: wifi_signal
      name: "WiFi Signal Sensor"
      update_interval: 60s
  ```
  2. Validate and upload.
  3. You can add the block on your dashboard to show the date (in db)
  ![](https://github.com/Gry1995/Iot-Project/blob/master/ESPHome%20installation%20and%20setting/sensor.PNG)
  > It shows unavailable because the ESP8266 is power off
  Follow [offical documents] to achive more functions of IoT.


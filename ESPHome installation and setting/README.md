# ESPHome installation and setting
> ESPHome is a system to control your ESP8266/ESP32 by simple yet powerful configuration files and control them remotely through Home Automation systems.
![](https://esphome.io/_images/logo-text.svg)
# Hardware
  1. There are many kinds of hardware support ESPhome: `ESP8266`, `ESP8266 NodeMCU`, `ESP32` and `ESP32 NodeMCU`. And there are also many versions, so be careful the differences of serial port and pin point.
  2. Here I use the `ESP8266 NodeMCUv3`, a latest version with a `CH340` serial port. And I list the reasons why I chose this one:
    * It is natively supported by the integration of `HASS.io`, it can be managed very easily.
    * It has enough GPIOs to connect and test, even provide an `ADC pin`, better than `Raspberry Pi`.
    * After connected to Wi-Fi, it can be flashed and uploaded OTA(over-the-air), no wire needed.
    * It is cheap enough, about 5$.
    * The `.yaml` file is easy to configure. Moreover, you could use `ESPeasy` firmware to help you. ([ESPeasy](https://www.letscontrolit.com/wiki/index.php/ESPEasy))

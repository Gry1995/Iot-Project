# HASS.io control GPIO of Pi
## 1. Hardwares
    * RF launcher
    
    * RF controlled relay
    * Dupont wire
## 2. Launcher Wire Connection
    1. `VCC` connect to `pin 2`.
    2. `GND` connect to `pin 14`.
    3. `K1` connect to `pin 16` also `BCM 23`.
## 3. Relay Wire Connection
    1. Connect to the 12V power supply.
    2. Control terminal connect to junmper of the PC motherboard or other low voltage devices.
## 4. Configuration.yaml Edit
    1. You can find examples on the [official document.](https://www.home-assistant.io/integrations/rpi_gpio/#switch)
    2. Add attached code under sensor type.
    ```python
    switch:
    - platform: rpi_gpio
      invert_logic: true
      ports:
        23: PC
    ```
    3. Rebbot the HASS.io.
      

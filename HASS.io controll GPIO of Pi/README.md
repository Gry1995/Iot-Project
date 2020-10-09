# HASS.io control GPIO of Pi
  ![]()
## 1. Hardwares
  * RF launcher
  ![](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20controll%20GPIO%20of%20Pi/IMG_3092.jpg)
  * RF controlled relay
  ![](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20controll%20GPIO%20of%20Pi/IMG_3093.jpg)
  * Dupont wire
## 2. Launcher Wire Connection
  1. `VCC` connect to `pin 2`.
  2. `GND` connect to `pin 14`.
  3. `K1` connect to `pin 16` also `BCM 23`.
  4. Connect a long Dupont wire to the `pin ant` if you don't have any antenna.
  ![](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20controll%20GPIO%20of%20Pi/IMG_3089.jpg)
  ![](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20controll%20GPIO%20of%20Pi/IMG_3090.jpg)
## 3. Relay Wire Connection
  1. Connect to the 12V power supply.
  2. Control terminal connect to junmper of the PC motherboard or other low voltage devices.
  ![](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20controll%20GPIO%20of%20Pi/IMG_3095.jpg)
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
## 5. RF Code Learning
  1. Press learning button and send RF signal on web UI or Homekit.
  ![](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20controll%20GPIO%20of%20Pi/IMG_3091.PNG)
  ![](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20controll%20GPIO%20of%20Pi/pc.PNG)
  2. You will find the red led switch on, which means the RF launcher is sending signal and your PC will power on.
## 6. Display Problem
  1. The button of PC will always be displayed as on after you sent the RF signal, but in fact, the relay turns off after an instant on. And this problem can not be fixed at Configuration.yaml.
  2. Here I use automation to solve this problem.
  3. Setup a new automation
  ```python
    trigger:
      - platform: state
        entity_id: switch.pc
        from: 'off'
        to: 'on'
      condition: []
    action:
      - delay: '0.5'
      - service: switch.turn_off
        data: {}
        entity_id: switch.pc
    mode: single
  ```
  4. When the state of PC change from off to on, the system will call the `service: switch turn off` after 0.5 second. 
      

# Control RGB light strip
  1. Read [offical document](https://esphome.io/components/light/rgb.html) of RGB controlling on ESPHome.
  2. Edit the ESPHome firmware file, same as before [project]().
  3. Add codes under `light` type:
  ```python
      light:
      - platform: rgb
        name: "RGB Light"
        red: output_component1
        green: output_component2
        blue: output_component3

    output:
      - platform: esp8266_pwm
        id: output_component1
        frequency: 1000 Hz
        pin: D1

      - platform: esp8266_pwm
        id: output_component2
        frequency: 1000 Hz
        pin: D2
    
      - platform: esp8266_pwm
        id: output_component3
        frequency: 1000 Hz
        pin: D3
  ```
  4. Connect wires following the definition of the pins in the file.
  ![]()
  ![]()
  5. The light entity will add to HASS.io automatically.
  ![]()
  ![]()
  6. Now the RGB light strip can be controlled on Home Assistant.
  ![]()

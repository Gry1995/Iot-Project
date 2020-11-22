# Smart home automation based on Home-Assistant.io
## Prerequired project:
### [Home Assistant installation](https://github.com/Gry1995/Iot-Project/tree/master/HASS.io%20installation)
### [GPIO control on HASS.io](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20controll%20GPIO%20of%20Pi/README.md)
### [ESPHome installation and setting](https://github.com/Gry1995/Iot-Project/tree/master/ESPHome%20installation%20and%20setting)
### [TTS (Text-to-Speech) on HASS.io](https://github.com/Gry1995/Iot-Project/tree/master/TTS%20on%20Homeassistant.io)

    These are projects which I created and finished before, I will use them to make some automation here.

## Useful information and tools of the Home Assistant automation 

### Developer Tools: 

  `Developer tools` is original function of HASS.io. It has 4 tabs: `States`, `services`, `template` and `events`. Especially for the first tab, in subsequent projects it is 
often necessary to monitor the states and attributes of the entity.
  
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/tab.png)
  
  In order to return desired state or attributes. Here are some templates of entity weather.my_home:
  1. To return all current states and attributes: 
  ```python
  data: 
    information: {{states.weather.my_home}} # Will return partlycloudy, -1, 51, 1040.2 ······
  ```
  2. To return current state:
  ```python
  data: 
    information: {{states.weather.my_home.state}} # Will return partlycloudy.
  ```
  3. To return all attributes:
  ```python
  data: 
    information: {{states.weather.my_home.attributes}} # Will return -1, 51, 1040.2 ······
  ```
  4. To return specific attribute:
  ```python
  data: 
    information: {{states.weather.my_home.attributes.temperature}} # Will return -1.
  ```

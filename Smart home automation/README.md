# Smart Home Automation Based on Home-Assistant.io
## 1. Prerequired project:

   These are projects which I created and finished before, I will use them to make some automation here.

* ### [Home Assistant installation](https://github.com/Gry1995/Iot-Project/tree/master/HASS.io%20installation)
* ### [GPIO control on HASS.io](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20controll%20GPIO%20of%20Pi/README.md)
* ### [ESPHome installation and setting](https://github.com/Gry1995/Iot-Project/tree/master/ESPHome%20installation%20and%20setting)
* ### [TTS (Text-to-Speech) on HASS.io](https://github.com/Gry1995/Iot-Project/tree/master/TTS%20on%20Homeassistant.io)
* ### [Add Google Calendar to HASS.io](https://github.com/Gry1995/Iot-Project/blob/master/Add%20Google%20Calendar%20to%20HASS.io/README.md)

![]()

## 2. Useful information and tools of the Home Assistant automation 

![]()

### 2.1 Developer Tools: 

  * `Developer tools` is original function of HASS.io. It has 4 tabs: `States`, `services`, `template` and `events`. Especially for the first tab, in subsequent projects it is  necessary to monitor the states and attributes of the entity.
  
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/tab.png)
  
  * In order to return desired state or attributes. Here are some templates of entity weather.my_home:
  
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

![]()

### 2.2 Automation editing tool

  * There are two ways to create automation of entities: Editing `automation.yaml` and using `automation editing tool`. Automation editing tool is very useful and easy to understand for novice.
  * Also the UI format can be converted to yaml format easy to copy and paste.
  * More information can be found at [offical website](https://www.home-assistant.io/integrations/automation).
  
![]()

  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/auto%20(1).png)
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/auto%20(2).png)
  
      Basic settings of automation editing tool
      
![]()

  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/auto%20(3).png)
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/auto%20(4).png)
  
      Convert to yaml format
    
## 3. External network control

  * HASS.io is generally used as an internal network server, which means that if you want to control entities in the network, the control devices and the Raspberry Pi should to be under the same Wi-Fi. So how to realize remote control through external network is a problem. 
  * Generally, port mapping is used, but it is not recommended. Because there is a risk of privacy and hacking. Here I will use two tricks: HomeKit and Google calendar.

![]()

### 3.1 HomeKit external control
 
  * Since the lastest version of HASS.io native support HomeKit, [Homebridge](https://www.npmjs.com/package/homebridge) is no longer needed. Use HomeKit to control devices is convenient. However, if you want external control function, you have to set up your HomePod, HomePod mini, Apple TV, or iPad as a [Home Hub](https://support.apple.com/en-us/HT207057). Also the home hub must connect to the same Wi-Fi as Raspberry Pi's.
  ![](https://support.apple.com/library/content/dam/edam/applecare/images/en_US/homepod/ios14-homepod-mini-apple-tv-automation-hero.jpg)

![]()

### 3.2 Google calendar external control
  After adding Google calendar to HASS.io, the calendar account will create some sensors. By reading the attributes of these sensors, they can be used as a specific trigger to complete a series of automation. Relate [project](https://github.com/Gry1995/Iot-Project/blob/master/Add%20Google%20Calendar%20to%20HASS.io/README.md) 
  * The system will check the calendar sometimes, and sensor attributes will follow the nearest event on calendar.
  * Sensor attributes include `offset_reached`, `all_day`, `message`, `description`, `location`, `start_time`and `end_time`. 
  * Attributes detail can be found [here](https://www.home-assistant.io/integrations/calendar.google/#sensor-attributes).

### 3.3 An example of external control
  Sometimes you may want to turn off the light which connected to the HASS.io at a specific time, but you will not at home at that time. The most convenient external control way is use HomeKit. However if you don't have any IOS devices or a `Home Hub`. You could use the second way: Google calendar external control.
  * `Remember`: The calendar sensor can detect your update at any time, but it does not mean that the system can automatically trigger the response switch. You must set up various automation solutions in advance.
  
  
  
  
  
  
  
  To be update.

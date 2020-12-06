# Smart Home Automation Based on Home-Assistant.io
## 0. Catalog:
* ### [Prerequired project](https://github.com/Gry1995/Iot-Project/tree/master/Smart%20home%20automation#1-prerequired-project)
* ### [Useful information and tools of the Home Assistant automation](https://github.com/Gry1995/Iot-Project/tree/master/Smart%20home%20automation#2-useful-information-and-tools-of-the-home-assistant-automation)
   * Developer Tools
   * Automation editing tool
* ### [External network control](https://github.com/Gry1995/Iot-Project/tree/master/Smart%20home%20automation#3-external-network-control)
   * HomeKit external control
   * Google calendar external control
   * An example of external control
* ### [Voice message reminder automation](https://github.com/Gry1995/Iot-Project/tree/master/Smart%20home%20automation#4-voice-message-reminder-automation)
  * TTS installation
  * TTS function test
  * Using TTS service to do some automation
* ### Plans in the future
**** 
## 1. Prerequired project:

   These are projects which I created and finished before, I will use them to make some automation here.

* ### [Home Assistant installation](https://github.com/Gry1995/Iot-Project/tree/master/HASS.io%20installation)
* ### [GPIO control on HASS.io](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20controll%20GPIO%20of%20Pi/README.md)
* ### [ESPHome installation and setting](https://github.com/Gry1995/Iot-Project/tree/master/ESPHome%20installation%20and%20setting)
* ### [TTS (Text-to-Speech) on HASS.io](https://github.com/Gry1995/Iot-Project/tree/master/TTS%20on%20Homeassistant.io)
* ### [Add Google Calendar to HASS.io](https://github.com/Gry1995/Iot-Project/blob/master/Add%20Google%20Calendar%20to%20HASS.io/README.md)
**** 

## 2. Useful information and tools of the Home Assistant automation: 

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

### 2.2 Automation editing tool:

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
****     
## 3. External network control:

  * HASS.io is generally used as an internal network server, which means that if you want to control entities in the network, the control devices and the Raspberry Pi should to be under the same Wi-Fi. So how to realize remote control through external network is a problem. 
  * Generally, port mapping is used, but it is not recommended. Because there is a risk of privacy and hacking. Here I will use two tricks: HomeKit and Google calendar.

![]()

### 3.1 HomeKit external control:
 
  * Since the lastest version of HASS.io native support HomeKit, [Homebridge](https://www.npmjs.com/package/homebridge) is no longer needed. Use HomeKit to control devices is convenient. However, if you want external control function, you have to set up your HomePod, HomePod mini, Apple TV, or iPad as a [Home Hub](https://support.apple.com/en-us/HT207057). Also the home hub must connect to the same Wi-Fi as Raspberry Pi's.
  ![](https://support.apple.com/library/content/dam/edam/applecare/images/en_US/homepod/ios14-homepod-mini-apple-tv-automation-hero.jpg)

![]()

### 3.2 Google calendar external control:
  After adding Google calendar to HASS.io, the calendar account will create some sensors. By reading the attributes of these sensors, they can be used as a specific trigger to complete a series of automation. Relate [project](https://github.com/Gry1995/Iot-Project/blob/master/Add%20Google%20Calendar%20to%20HASS.io/README.md) 
  * The system will check the calendar sometimes, and sensor attributes will follow the nearest event on calendar.
  * Sensor attributes include `offset_reached`, `all_day`, `message`, `description`, `location`, `start_time`and `end_time`. 
  * Attributes detail can be found [here](https://www.home-assistant.io/integrations/calendar.google/#sensor-attributes).

### 3.3 An example of external control:
  Sometimes you may want to turn on the light which connected to the HASS.io at a specific time, but you will not at home at that time. The most convenient external control way is use HomeKit. However if you don't have any IOS devices or a `Home Hub`. You could use the second way: Google calendar external control.
  * #### Remember: The calendar sensor can detect your update at any time, but it does not mean that the system can automatically trigger the response switch. You must set up various automation solutions in advance.
  * Create an automation: 
    1. First we have to define some states of your attribute. That will help system know which devices we are going to use. Such as we define `kitchen light on` as a key word.
    2. We have to define which attribute to use: `message` or `description`, these definitions don't need to be set on system, that are the rules made by yourself.
    3. Here we select attribute `message` and create a nearest new event `title`: kitchen light on.
    ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/calendar%201.PNG)
    4. Fresh the system and we will find a message attribute of the calendar is `kitchen light on`.
    ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/entity%201%20condition.PNG)
    5. Create a new automation, `triggers type`: states, `entity`: Calendar id, `attribute` `to` kitchen light on. Add another trigger, `triggers type`: states, `entity`: Calendar id, `to`: on
    6. Set actions and conditions meet the needs of reality.
    ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/trigger%201.PNG)
    ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/trigger%202.PNG)
    7. Delete the event on calendar and fresh the HASS.io system.
    8. Next time when the calendar sensor read the `kitchen light on` message again, the automation will excute.
  * ### Because multiple attributes of the calendar sensor can be read, we can add some details when creating the event, for example, here I added the `location` and `time`. On the status page we can see the difference from before.
  * ### Another thing we need to pay attention to is that the status of the sensor (On or Off) depends on whether there is an event on the calendar at the current time. If there is an all-day event, the state of the sensor shall be `On` for a long time, and the impact on the attribute is still being tested.
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/calendar%202.PNG)
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/entity%202%20condition.PNG)
**** 
## 4. Voice message reminder automation: 
  Voice reminder is a very useful and convenient part of smart home automation. At previous project, we have already added [TTS(Text-to-Speech)](https://github.com/Gry1995/Iot-Project/tree/master/TTS%20on%20Homeassistant.io) function to HASS.io, I can use this feature to improve my Smart Home Automation.

### 4.1 TTS installation
  More detail and method please refer my [previous project](https://github.com/Gry1995/Iot-Project/blob/master/TTS%20on%20Homeassistant.io/README.md).
  [Baidu Cloud](https://login.bce.baidu.com/?lang=en) offers many useful `Ais` and `APIs`, and most of them are free for students such as `Speech Synthesis API`.
  1. Create a program on Baidu `Speech Synthesis API`, and system will generate `app_id` `api_key` `secret_key`, we will need them when we edit the `configuration.yaml` file. 
  2. Click on English or Chinese language pack, you will have three months credit to use this servise for free.
  3. Edit `configuration.yaml` file to open TTS function.
  ```python
    tts:   
      - platform: baidu      
        app_id: xxxxxxxxxxxx
        api_key: xxxxxxxxxxxxxxxxxxxx
        secret_key: xxxxxxxxxxxxxxxxxxxxxxx
        speed: 5     
        pitch: 5     
        volume: 15     
        person: 0
  ```
  
  4. Using `MPD` to add the speaker to HASS. [Mopidy](https://docs.mopidy.com/en/latest/installation/) is an extensible music server written in Python.
  5. Add the archive’s GPG key:
  ```python
    wget -q -O - https://apt.mopidy.com/mopidy.gpg | sudo apt-key add -
  ```
  ****
  6. Add the APT repo to your package sources:
  
  ```python
    sudo wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/buster.list
  ```
  ****
  7. Install `Mopidy` and all dependencies:
  ```python
    sudo apt install mopidy
  ```
  ****
  8. To install `MPD`:
  ```python
    sudo apt install mopidy-mpd
  ```
  > More intsallation https://docs.mopidy.com/en/latest/installation/
  ****
  9. Edit or create `/etc/mopidy/mopidy.conf` file, add a `MPD` section.
  ```python
    [mpd]
    enabled = true
    hostname = 127.0.0.1
    port = 6600
  ```
  Or
  ```python
    [mpd]
  ```
  10. Running as a service:
  ```python
    sudo systemctl start mopidy 
  ```
  > Other command:https://docs.mopidy.com/en/latest/running/service/#service-management-on-debian
  
  
### 4.1 TTS function test
  
  1. Add a card of MPD speaker to the dashboard on your HASS.
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/card%20configuration.PNG)
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/MPD%20cartd.PNG)
  2. Connect speaker to your Raspberry Pi or other devices.
  3. Text some words or speechs on the `Text to speak` bar to test.
  
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/speak.PNG)
  
  4. You will hear the speaker speak words you texted.
  5. If the step 4 not working, check the history of MPD devices. When the card is showing `off` and was triggered normally, check API and hardware. When the card is showing `unavailable`, please check if MPD server is working or ports does not conflict.
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/triggered.PNG)
> Triggered history
    
### 4.2 Using TTS service to do some automation

  1. The key service is `tts.baidu_say` or `tts.google_say`. The entity is `media_player.mpd`. 
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/entity%20mpd.PNG)
  
  2. Create an automation and edit `Action` and `Triggers` section. Here is an example of telling temprature at a specific time on calendar. 
  3. Like [steps](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/README.md#33-an-example-of-external-control) on 3.3 section `triggers type`: states, `entity`: Calendar id, `attribute` `to` tell the temprature. Add another trigger, `triggers type`: states, `entity`: Calendar id, `to`: on. 
  4. As I mentioned before, `Developer Tools` offers some important states we needed. For temprature we need the function below.

> To return specific attribute:
>  ```python
>  data: 
>    information: {{states.weather.my_home.attributes.temperature}} # Will return -1.
>  ```

  5. Edit `Action` section in `UI` or `yaml`.
  ```python  
  service: tts.baidu_say
  data:
    entity_id: media_player.mpd
    message: 'temprature is {{states.weather.my_home.attributes.temperature}}'
  ```
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/call%20service.PNG)
> In UI configuration
  
  6. Save the automation and open it, as soon as the calendar detect the title `tell the temprature`, the speaker will tell you the temprature at that time.
  7. With more python scripts and settings, we can achieve more and smarter automation on our system.
****   
### 5. Plans in the future
  #### Voice interaction is a very important function in `IoT`. At present, in terms of interaction, we can only automatically obtain current information through `TTS`, but not through the microphone to tell the system what we need. Joining the AI assistant is an idea, or we can set up a simple voice recognition service： Trigger the specified automated service by detecting the keywords we say. 
  When setting up `Baidu TTS`, I noticed that they also provide a `speech recognition API`, but it is not natively supported by `HASS.io`. In the future, I will try to use the community support in `HACS` ([Everything about HACS](https://hacs.xyz/)) and `Addon-Store` ([How to use Addon-store at my previous steps record](https://github.com/Gry1995/Iot-Project/tree/master/HASS.io%20installation#3-supervisor-offers-you-many-of-great-features-recommended-install-mqtt-and-file-editor)) to complete the goal of voice interaction.

![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/Addon%20store%20support.PNG)
> Addon-store

![](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/Pictures/HACS.PNG)
> HACS

## [Back to top](https://github.com/Gry1995/Iot-Project/blob/master/Smart%20home%20automation/README.md#smart-home-automation-based-on-home-assistantio)

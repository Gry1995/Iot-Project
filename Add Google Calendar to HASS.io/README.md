# Add Google Calendar to HASS.io

## 1. Introduction

> The google calendar platform allows you to connect to your Google Calendars and generate binary sensors. The sensors created can trigger based on any event on the calendar or only for matching events. Cite from [Google Calendar Event](https://www.home-assistant.io/integrations/calendar.google/

  Many devices automations are based on specific time. Add a calendar platform to HASS.io could save a lot of time to set up repetitive tasks. What's more, calendar accounts are also can also be regarded as a log. You can monitor specific function triggers without checking out background records.


![](blank)

## 2. Prerequisites
  
  * `Official guide` can be found [here](https://www.home-assistant.io/integrations/calendar.google/#prerequisites)
  * After Google APIs website updated, some steps in `Official guide` are no longer applicable. But overall is doable.
  * Some tips can be found below:
    1. When adding credentials to your project, you should select `Google calendar API` and `Other UI`.
    2. Just select `External` and click `Create` button to set up OAuth consent screen.
    3. After create OAuth consent screen, guide to `Credentials` in the left and then click on `+ Create credentials`.
    4. Choose the Application type: `TVs and Limited input devices` and create.
    5. After creation, you will get two keys `client ID` and `client secret` similar to the figure below.
    6. Then add keys to configuration.yaml.
     ```python
    # Example configuration.yaml entry
    google:
      client_id: YOUR_CLIENT_ID
      client_secret: YOUR_CLIENT_SECRET
    ``` 

![](https://github.com/Gry1995/Iot-Project/blob/master/Add%20Google%20Calendar%20to%20HASS.io/keys.PNG)

![](https://github.com/Gry1995/Iot-Project/blob/master/Add%20Google%20Calendar%20to%20HASS.io/two%20keys.PNG)

  * Restarting the server may take more time than usual, After rebooting, two-step authentication is required in the message bar.
  
![](https://github.com/Gry1995/Iot-Project/blob/master/Add%20Google%20Calendar%20to%20HASS.io/message.png)

## 3. Features and settings

On progress


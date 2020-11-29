# Add Google Calendar to HASS.io

## 1. Introduction

> The google calendar platform allows you to connect to your Google Calendars and generate binary sensors. The sensors created can trigger based on any event on the calendar or only for matching events. Cite from [Google Calendar Event](https://www.home-assistant.io/integrations/calendar.google/

  Many devices automations are based on specific time. Add a calendar platform to HASS.io could save a lot of time to set up repetitive tasks. What's more, calendar accounts are also can also be regarded as a log. You can monitor specific function triggers without checking out background records.


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

![]()

     ```python
    # Example configuration.yaml entry
    google:
      client_id: YOUR_CLIENT_ID
      client_secret: YOUR_CLIENT_SECRET
    ``` 

![](https://github.com/Gry1995/Iot-Project/blob/master/Add%20Google%20Calendar%20to%20HASS.io/keys.PNG)

![](https://github.com/Gry1995/Iot-Project/blob/master/Add%20Google%20Calendar%20to%20HASS.io/two%20keys.PNG)

![](blank)

  * Restarting the server may take more time than usual, After rebooting, two-step authentication is required in the message bar.
 
![](blank)
 
![](https://github.com/Gry1995/Iot-Project/blob/master/Add%20Google%20Calendar%20to%20HASS.io/message.png)



## 3. Features and settings

  * After adding Google Calendar to HASS.io, the system will create a `google_calendars.yaml` file. This file will generate some sensors based on your google calendar account. If you want to use one of them, you have to copy and paste the `cal_id` to the blank of entity.

### 3.1 Create events and dates to calendar

  * In order to add events to calender. You have to call the service of `google.add_event`, fullfill the `cal_id` and `summary`. The `cal_id` is The id of the calendar you want, `summary` is the title of the event.
  * Optional you can also add `description`, `start_date_time`, `end_date_time` and other [service data attributes](https://www.home-assistant.io/integrations/calendar.google/#service-googleadd_event).
  * Here is an example to add message 'test calendar'.
  ```python
    service: google.add_event
    data:
      calendar_id: find at google_calendars.yaml
      summary: 'test calendar'
  ```

### 3.2 Using calendar as sensor

  * The system will check the calendar sometimes, and sensor attributes will follow the nearest event on calendar.
  * Sensor attributes include `offset_reached`, `all_day`, `message`, `description`, `location`, `start_time`and `end_time`. 
  * Attributes detail can be found [here](https://www.home-assistant.io/integrations/calendar.google/#sensor-attributes).
  * By reading the attributes of the calendar, it can be used as a specific trigger to complete a series of automation.

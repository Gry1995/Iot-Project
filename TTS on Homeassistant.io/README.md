# TTS(Text-to-Speech) on Homeassistant.io
Now AI is a very important part of IoT, many platforms have their own AI assitants. However, Home Assistant does not offer one. Here I want use a simple ways: `TTS` to design my own assistant. Not so smart, but can help me a lot.
## Method #1 Google translate TTS
  [Google translate](https://translate.google.com/) TTS method is a very tricky and interesting way. We can use the basic function of Google translate to generate the speech we need.
  1. HASS supports Google translate TTS natively, so we can add this part to the `configuration.yaml` directly.
  ```python
  
  tts:
  - platform: google_translate
  # Offical Introduction: https://www.home-assistant.io/integrations/tts#configuring-a-tts-platform
  
  ```
  2. Next we can call the `tts.google_translate_say` service to say something.
  ```python
  
  # A sample of Google translate TTS service
  
  service: tts.google_translate_say
  entity_id: media_player.mpd # The speaker
  data:
    message: 'Bonjour' # The text you want to speech
    language: 'fr' # The language you are using
    
  ```
  3. However your HASS maybe is running on docker, adding the speaker to HASS as an entity need more things to do. I am going to finish it in the next part.

## Method #2 Using API of Baidu TTS
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
## Install Mopidy on Raspberry Pi to active MPD
  Above we added TTS servise on HASS. However, HASS maybe is running on docker, adding the speaker to HASS as an entity need a transfer. We use MPD here.
  1. [Mopidy](https://docs.mopidy.com/en/latest/installation/) is an extensible music server written in Python.
  2. Add the archive’s GPG key:
  ```python
    wget -q -O - https://apt.mopidy.com/mopidy.gpg | sudo apt-key add -
  ```
  3. Add the APT repo to your package sources:
  ```python
    sudo wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/buster.list
  ```
  4. Install `Mopidy` and all dependencies:
  ```python
    sudo apt install mopidy
  ```
  5. To install `MPD`:
  ```python
    sudo apt install mopidy-mpd
  ```
  > More intsallation https://docs.mopidy.com/en/latest/installation/

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
  3. 

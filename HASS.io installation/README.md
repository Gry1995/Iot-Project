# Install Home Assistant to Raspberry Pi (Use Docker):
## 1. Install Docker
  1. Change source if you are outside of US or UK.
  2. Install docker
  ```python
  curl -sSL https://get.docker.com | sh
  ```
  3. Change docker source if needed.
  ```python
  sudo nano /etc/docker/daemon.json
  
  {
  "registry-mirrors": ["https://registry.docker-cn.com"] # A cn source
  }
  ```
  4. Restart docker.
  ```python
  sudo systemctl restart docker
  ```
  5. Install a GUI for docker (Portainer for example)
  ```python
  docker pull  portainer/portainer:linux-arm
  # Open it at port 9000
  docker run -d --name portainer --restart unless-stopped -p 9000:9000 -v ~/portaniner/data:/data -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer:linux-arm
  ```
  
![]()  
  
## 2. Pull and install HASS.io
  1. Install Home Assistant Supervised
  ```python
  sudo su
  curl -sL https://raw.githubusercontent.com/home-assistant/supervised-installer/master/installer.sh | bash -s
  ```
  >cite from https://github.com/home-assistant/supervised-installer
  2. Use http://IP:8123 to enter the GUI of HASS.io
  2. Read [Docs](https://www.home-assistant.io/docs/0) for help.
  3. Get HomeKit component if you want to control your devices by iOS or MacOS.
  
![]()

## 3. Tips
  ### 1. After several updates in 2020, many community functions have been integrated into the integration, which made many early tutorials no longer applicable. Searching integration and configuring integration need refer to [official documents.](https://www.home-assistant.io/integrations/)
  #### 2. There are other ways to install Home Assistant. You can compare them [here.](https://www.home-assistant.io/docs/installation/)
  ### 3. Supervisor offers you many of great features. Recommended install `MQTT` and `File editor`. 
  
  ![](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20installation/addon.PNG)
  
  ### 4. Also you could add other repositories to your Addon store.
  
  ![](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20installation/repositories.PNG)
  
  ### 5. `File editor` add-on allow you to write configurations on a web UI. The `configuration.yaml` is the most important file, some of integrations required to be setup here.
  
  ![](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20installation/webUI.PNG)
  
  ### 6. New version of HASS.io offers web UI to configure Automations, Scenes and Scripts, but you can also write them manually on `Scenes.yaml` `Scripts.yaml` `Automations.yaml`. 
  ### 7. Some community features may not include in Addon store or Integration. You can add them by create a folder under `/config/custom_components/`.
  ### 8. After changing the `configuration.yaml` you may have to reboot the HASS.io.
  
  ![](https://github.com/Gry1995/Iot-Project/blob/master/HASS.io%20installation/reboot.PNG)

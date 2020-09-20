# Lab 02 install Home Assistant to raspberry Pi (use docker):
## 1. Install docker
  1. Change source if you are outside of US or UK.
  2. Install docker
  ```python
  curl -sSL https://get.docker.com | sh
  ```
  3. Change docker source if needed.
  ```python
  sudo nano /etc/docker/daemon.json
  
  {
  "registry-mirrors": ["https://registry.docker-cn.com"] #A cn source
  }
  ```
  4. Restart docker.
  ```python
  sudo systemctl restart docker
  ```
  5. Install a GUI for docker(portainer for example)
  ```python
  docker pull  portainer/portainer:linux-arm
  # Open it at port 9000
  docker run -d --name portainer --restart unless-stopped -p 9000:9000 -v ~/portaniner/data:/data -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer:linux-arm
  ```
## 2. Pull and install HASSIO
  1. Install Home Assistant Supervised
  ```python
  sudo su
  curl -sL https://raw.githubusercontent.com/home-assistant/supervised-installer/master/installer.sh | bash -s
  ```
  >cite from https://github.com/home-assistant/supervised-installer
  2. Use IP:8123 to enter GUI of HA
  2. Read [Docs](https://www.home-assistant.io/docs/0) for help.
  3. Get HomeKit component if you want to controll your devices by iOS or MacOS.

# Lesson1 steps and code:
## 1. Configuration
  1. Copy OS to tf card and intall it.
  
  2. Reset password and connect Wi-Fi.
  
  3. Get IP address.
## 2. Install VNC
  1. Open Terminal and clone code.
  ```python
  sudo raspi-config
  ```
  2. Interfacing `Options` -> `VNC` -> `Yes`.
  3. Download VNC from [site](https://www.realvnc.com/en/connect/download/viewer/).
  4. Use ip, pw and user name to login.
## 3. Startup Mailer
  1. Can't generate Gmail 2-step password, use other e-mail instead.
  2. Switch ```smtp``` on and get ```authorization code``` and ```host```.
  3. Create and edit ```[mailer.py](https://github.com/Gry1995/Iot-Project/blob/master/Lesson01/mailer.py)```.
  4. Edit ```rc.local``` to sent e-mail when reboot.
  ```python
  sudo nano /etc/rc.local
  python /home/pi/mailer.py
  ```
  ![](https://github.com/Gry1995/Iot-Project/blob/master/Lesson01/IP%20address.PNG)

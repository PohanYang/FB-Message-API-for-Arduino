# Facebook message control Arduino  
  
  
In this project, we can use facebook message to control arduino signal  
### Requirement:  
  1. Arduino Microcontroller (I use Arduino Uno SMD R3)  
  2. A PC have python(2.7 up)  
  3. A breadboard, LED...etc. Others you want to control on arduino  
  
First, your PC need 2 application:
  1.pickle  <https://docs.python.org/3/library/pickle.html>  
  2.fbchat  <https://pypi.python.org/pypi/fbchat>  
You can install it from URL

And compile fbapi.ino to your arduino.  
Finally, you can run facebookAPIforArduino.py  
  
> $python facebookAPIforArduino.py fb1_id fb1_password fb2_id your_port  
  
fb1 is a facebook account for recived message to control arduino.  
fb2 is a facebook account for send message to remote.  
  
for example:  
> $python facebookAPIforArduino.py 100000161389416 xxxxxxxx 100000161389555 COM3  
  
### Demo test:  
In fbapi.ino we write 5 case to control LED on arduino, when we sent '1' and logit port 13 output LED will be bright.  
'0' is turn off all LED.  
Demo Video: <https://www.youtube.com/watch?v=AMp_If4aTmg&feature=youtu.be>  

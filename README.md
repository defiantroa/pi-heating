# pi-heating
Some scripts tweaked from https://github.com/JeffreyPowell


Installation
=============================

$ wget "https://github.com/jonsag/pi-heating/archive/0.2.tar.gz" -O "/home/pi/pi-heating.tar.gz"
$ cd /home/pi
$ tar -xvzf pi-heating.tar.gz
or
$ cd /home/pi
$ git clone https://github.com/jonsag/pi-heating.git

$ cd /home/pi/pi-heating

On pi running as hub or hub/remote:
-----------------------------
$ sudo ./pi-heating-hub-install.sh
$ sudo ./pi-heating-hub-mysql-install.sh
$ sudo ./pi-heating-hub-secure.sh


If hub also will have extended weather and power logging:
-----------------------------
$ sudo ./pi-heating-extended-log-install.sh
		$ wget "http://www.triconsole.com/php/calendar_download.php" -O "/home/pi/calendar.zip"

Build arduino-power-logger
Edit sketch passive_logger_no_time_static_ip.ino
Change lines 41-43
	byte mac[] = {  
	  0x90, 0xA2, 0xDA, 0x0C, 0x00, 0x76 }; // MAC address, printed on a sticker on the shield
	IPAddress ip(192,168,10,10); // ethernet shields wanted IP
to your boards MAC and desired IP

Start up your arduino hooked up to your LAN

Edit /var/www/pi-heating-extended-log/config.php
Change lines 24-25
	$powerUrl = 'http://192.168.10.10';
	$powerPollReset = 'http://192.168.10.10/?pollReset';
to same IP as above


On pi running solely as remote or as hub/remote:
-----------------------------
$ sudo ./pi-heating-remote-install.sh


On pi running as weather logger:
-----------------------------
$ sudo ./pi-heating-weather-install.sh

Add apache user to dialout and tty group
$ sudo usermod -a -G dialout, tty www-data

Reboot pi

Find out tty-device
$ dmesg | grep tty
Probably named someting like '/dev/ttyACM0'
Edit /var/www.pi-heating-weather/weather.php
Change line 32
	define("PORT","/dev/ttyACM0");
so it matches the output from above


Installing and running Arduino IDE:
=============================

Download Arduino IDE from https://www.arduino.cc/en/Main/Software
$ mv arduino-*.tar.xz ~/bin
$ cd ~/bin
$ tar -xvJf arduino-*.tar.xz
$ cd arduino-*
$ ./install.sh

Install Average library:
-----------------------------
Copy directory Average to your Arduino/libraries directory

Start Arduini IDE

Check settings and install sketch:
-----------------------------
Select Board and Port
Open sketch
Compile and upload to arduino

$ stty -F /dev/ttyUSB0 cs8 9600 ignbrk -brkint -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts
$ stty -F /dev/ttyS0 ispeed 9600 ospeed 9600 -ignpar cs8 -cstopb -echo
$ stty -F /dev/ttyACM0 ispeed 9600 ospeed 9600 -ignpar cs8 -cstopb -echo

Connect to arduino with screen:
$ screen /dev/ttyACM0 9600 -S <session name>
To get screen command promp, enter
[C-a] :
Then type
quit
and [Return]
	or from outside of screen
$ screen -X -S <session name> quit

Kill screen with ^ak or control-a k

$ rsync -rci ~/Documents/EclipseWorkspace/pi-heating/pi-heating-hub-extended-log/www/* pi@raspberry03:/var/www/pi-heating-hub-extended-log/











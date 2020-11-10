# Intro
This is a documention how to read the serial data from Aidon electricity meters based. My electricity provider is Tekniska Verken (Sweden) and it seems they adopted to an early version (1.2) of "Branschrekommendation för lokalt kundgränssnitt för elmätare".

# The HAN/P1/H1 port
The interface is a RJ12 female connector with pin assignments as shown in the figure below
![Alt text](img/aidon.png?raw=true "Interface")

When the data request, pin 2 is high (5V) then serial data will be sent on pin 5. The problem is that this is an open collector output, this means a logical 1 will be equal short to ground. A logical 0 will equal a floating connection. The Raspberry Pi used in this project require a logical 0 to be 0 V and a logical 1 to be 3.3 V on its serial input to function correctly. Also the lower level of 3.3 V of the RPi is lower than the 5 V output on the HAN port which needs to be considered. For this an inverter needs to be used as shown below.
![Alt text](img/schematic.png?raw=true "Interface")

Pins 1 and 2 on the RJ12 are shorted to have data request set to 5 V constantly.

When all this in place you should be able to run the serial read python program.

To read the binary file in you may use ''xxd filename.bin''

The next thing is to decode and parse the binary stream. It seems to be according to the A-XDR standard.



import serial, array
from datetime import datetime

ser = serial.Serial("/dev/ttyS0", 115200, timeout=1, parity=serial.PARITY_NONE)

start_time = datetime.now()
time_delta = datetime.now()-start_time
a = array.array('B', [])
while (11 > time_delta.total_seconds()):
	while ser.inWaiting():
		a.append(ord(ser.read(1)))
	time_delta = datetime.now()-start_time

print(a)

f = open("data/{}{}{}_{}{}{}.bin".format(start_time.year, start_time.month,start_time.day,start_time.hour,start_time.minute,start_time.second), "wb")
f.write(a)
f.close()


# print("{:02x} ".format(ord(ser.read(1))), end='')


ser.close()

import serial,time
from curses import ascii

modem = serial.Serial('/dev/ttyUSB2', 9600, timeout=1)

modem.write("AT+CMGF=1\r")
modem.readline()
status = modem.readline()

modem.write("AT+CNMI=1,1,0,1,0\r")
modem.readline()
status = modem.readline()

# modem.write('AT+CMGS="+441234567890"\r')
# modem.write("starting script")
# modem.write(ascii.ctrl('z'))

time.sleep(2)
# modem.readline()
# modem.readline()
# modem.readline()

# cmgi = modem.readline()
# print cmgi

# modem.readline()
# modem.readline()
# status = modem.readline()
# print status

print "Starting loop..."
while True:
	try:
		line = modem.readline()
		if line.startswith("+CMTI"):
			index = line.strip().split(":")
			(storage,location) = index[1].split(",")
			print "new SMS at %s, location %s" % (storage,location)
			# read the SMS here
			modem.write("AT+CMGR=%s\r" % location)
			time.sleep(2)
			modem.readline()
			header = modem.readline().strip()
			body = modem.readline().strip()
			modem.readline()
			status = modem.readline().strip()
			print "Status is: " + status
			# print header
			print body
			modem.write("AT+CMGD=%s\r" % location)
			modem.readline()
			status = modem.readline().strip()
			print status
		time.sleep(1)
	except:
		print "quitting"
		exit(0)

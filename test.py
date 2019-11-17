import obd
#obd.logger.setLevel(obd.logging.DEBUG)

#ports = obd.scan_serial()
#print ports
connection = obd.OBD(fast=False, timeout=30, check_voltage=False) # auto-connects to USB or RF port

cmd = obd.commands.SPEED # select an OBD command (sensor)

response = connection.query(cmd) # send the command, and parse the response

#print(response.value) # returns unit-bearing values thanks to Pint
#print(response.value.to("mph")) # user-friendly unit conversions

while(True):
	sleep(0.1)
	rpm = connection.query(obd.commands.RPM).value.magnitude
	print(rpm)

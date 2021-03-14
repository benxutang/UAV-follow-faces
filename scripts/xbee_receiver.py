from digi.xbee.devices import XBeeDevice

# Instantiate an XBee device object.
device = XBeeDevice("/dev/ttyUSB0", 115200)
device.open()

# Read data.
try:
    while True:
        xbee_message = device.read_data()
        
        if xbee_message != None:
            
            data = xbee_message.data.decode("utf8")
            print(data)
            
except KeyboardInterrupt:
    device.close()
    print('Ter')

from picamera import PiCamera
import time
import serial
import os
from digi.xbee.devices import XBeeDevice

print('Ready to go!')
string = input()

print('System in progress...')
camera = PiCamera()
camera.resolution = (640,480)

device = XBeeDevice("/dev/ttyUSB0", 115200)
device.open()
device.send_data_broadcast("Cam is open")
device.close()

device.open()

try:
    while True:
        time_01 = time.time()
        for i in range(1500):

            while True:
                
                time_02 = time.time()
                if time_02 - time_01 >= 0.8+ i*0.8:
                    
                    camera.capture('/home/pi/img%s.jpg' %i)
                    print('Complete')
                    break

                xbee_message = device.read_data()
        
                if xbee_message != None:
                    
                    data = xbee_message.data.decode("utf8")
                    print(data)

                    #uav_uart= serial.Serial(port='/dev/ttyAMA0', baudrate=115200, timeout=1)
                    #Hex_str = bytes.fromhex(data)
                    #uav_uart.write(Hex_str)
                

        i = 0
        
except KeyboardInterrupt:
    print('Terminalled.')

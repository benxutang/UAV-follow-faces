# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:54:59 2019

@author: LEN
"""


from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.devices import XBee64BitAddress
import time

device = XBeeDevice("COM16", 9600)
device.open()

time_01 = time.time()
try:
    while True:
        
        time_02 = time.time()
        
        if time_02 - time_01 >= 1 and time_02 - time_01 < 2:
            
            # Instantiate a remote XBee device object.
            remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041977F4A"))
            # Send data using the remote object.
            
            #d=0xffaa01020304
            
            str_d = 'ff aa 32 32 32 07'
            
            device.send_data_async(remote_device, str_d)
            print(str_d)
        
        if time_02 - time_01 >= 3 and time_02 - time_01 < 10:
            
            # Instantiate a remote XBee device object.
            remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041977F4A"))
            # Send data using the remote object.
            
            #d=0xffaa01020304
            
            str_d = 'ff aa 32 32 32 04'
            
            device.send_data_async(remote_device, str_d)
            print(str_d)
            
        if time_02 - time_01 >= 10 and time_02 - time_01 < 13:
            
            # Instantiate a remote XBee device object.
            remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041977F4A"))
            # Send data using the remote object.
            
            #d=0xffaa01020304
            
            str_d = 'ff aa 32 32 32 07'
            
            device.send_data_async(remote_device, str_d)
            print(str_d)
            
        if time_02 - time_01 >= 13 and time_02 - time_01 < 17:
            
            # Instantiate a remote XBee device object.
            remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041977F4A"))
            # Send data using the remote object.
            
            #d=0xffaa01020304
            
            str_d = 'ff aa 32 32 32 04'
            
            device.send_data_async(remote_device, str_d)
            print(str_d)
            
        if time_02 - time_01 >= 17 and time_02 - time_01 < 25:
            
            # Instantiate a remote XBee device object.
            remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20041977F4A"))
            # Send data using the remote object.
            
            #d=0xffaa01020304
            
            str_d = 'ff aa 32 32 32 09'
            
            device.send_data_async(remote_device, str_d)
            print(str_d)
            
        if time_02 - time_01 >= 25:
            
            break
    
    device.close() 
    print('Ter')
except KeyboardInterrupt:
    print('Ter')
    
python3 -m serial.tools.list_ports
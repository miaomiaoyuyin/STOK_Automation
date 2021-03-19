
from ppadb.client import Client as AdbClient
import time

# Default is "127.0.0.1" and 5037
adb = AdbClient(host="127.0.0.1", port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

concert = '1764 500'
start = '1781 977'
skip = '1984 990'
getPt = '1080 696'

#while True:
for i in range(22):
    #image = device.screencap()
    device.shell('input touchscreen tap ' + concert)
    time.sleep(1)
    device.shell('input touchscreen tap ' + start)
    time.sleep(1)
    device.shell('input touchscreen tap ' + start)
    time.sleep(28)
    device.shell('input touchscreen tap ' + skip)
    time.sleep(8)
    device.shell('input touchscreen tap ' + getPt)
    time.sleep(1)
    device.shell('input touchscreen tap ' + start)
    time.sleep(3)
    #with open('screen.png', 'wb') as f:
     #   f.write(image)
# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import machine
import pyb
import os
pyb.country('GB')  # ISO 3166-1 Alpha-2 code, eg US, GB, DE, AU

# https://pybd.io/hw/pybd_sfxw.html
# The board has a built-in micro SD card slot. If an SD card is inserted, by default it will not be automatically
# mount in the board’s filesystem but it will be exposed as a mass storage device if USB is used. To automatically
# mount the SD card if it is inserted, put the following in your boot.py:
if pyb.SDCard().present():
    os.mount(pyb.SDCard(), '/sd')
    pyb.usb_mode('VCP+MSC', msc=(pyb.Flash(), pyb.SDCard()))  # act as a serial and a storage device
else:
    pyb.usb_mode('VCP+MSC')  # act as a serial and a storage device

pyb.main('main.py')  # main script to run after this one




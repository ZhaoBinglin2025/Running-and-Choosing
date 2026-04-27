# This is a python-based serial to monitor whether our unity programm is sending markers that we want.

import serial

ser = serial.Serial("COM11", 115200, timeout=1)

print("Listening COM11...")

while True:
    data = ser.read(5)  

    if len(data) == 5:
        marker_byte = data[4]  

        marker = int(marker_byte)

        print("RAW:", data.hex(" "), "→ MARKER:", marker)

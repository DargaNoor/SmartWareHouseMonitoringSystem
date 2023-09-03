import serial
import time

data = serial.Serial(
                  'COM5',
                  baudrate = 9600,
                  parity=serial.PARITY_NONE,
                  stopbits=serial.STOPBITS_ONE,
                  bytesize=serial.EIGHTBITS,                  
                  timeout=1
                  )

def read_data():
    while True:
        d = data.readline()
        d = d.decode('UTF-8', 'ignore')
        print(d)
        if len(d) != 0:
            d = d.split(',')
            print(d)
            if len(d) > 4:
                break
    print(d[:-1])
    return d[:-1]

def read_data1():
    while True:
        d = data.readline()
        d = d.decode('UTF-8', 'ignore')
        print(d)
        if '54006E03172E' in d or '54006DFF6DAB' in d:
            break
    if '54006E03172E' in d:
        return '54006E03172E'
    if '54006DFF6DAB' in d:
        return '54006DFF6DAB'

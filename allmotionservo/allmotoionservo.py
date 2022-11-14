from time import sleep
import serial


class ServoMotor():
    
    def __init__(self, port=None):
        if port is not None:
            self.connect()

    def __exit__(self):
        self.disconnect()
        
    def connect(self, port='COM9'):
        if type(port) is int:
            port = 'COM%d'%port
        self.ser = serial.Serial(port=port, baudrate=9600, timeout=1, stopbits=1)

    def disconnect(self):
        self.ser.close()
        
    def move_absolute(self, pos):
        self.ser.write(b'/1A%d000R\r\n'%pos)

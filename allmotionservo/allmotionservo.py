import serial
import time 
import numpy as np

class ServoMotor():
    
    def __init__(self, port=None):
        if port is not None:
            self.connect(port)
            
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()
        
    def connect(self, port='COM9'):
        if type(port) is int:
            port = 'COM%d'%port
        self.ser = serial.Serial(port=port, baudrate=9600, timeout=1, stopbits=1)

    def disconnect(self):
        self.ser.close()
        
    def move_to_position(self, pos, relative=False):
        self.ser.write(b'/1A%dR\r\n'%pos)
        
    def _angle2pos(self, angle):
        return 256*angle/.9
        
    def move_to_angle(self, angle, relative=False):
        pos = self._angle2pos(angle)
        self.move_to_position(pos)

if __name__ == '__main__':
    with ServoMotor('COM9') as motor:
        motor.move_to_angle(0)
        time.sleep(5)
        for rotation in np.linspace(0,360,41):
            motor.move_to_angle(rotation)
            time.sleep(.2)
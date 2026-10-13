from getopt import error

import pigpio
import time

# Establish the necessary PWM signal widths/durations (in microseconds)
armCloseWidth = 1600
armNeutralWidth = 1500
armOpenWidth = 1400

class Arm:
    """Create and manage arm"""

    def __init__(self, pigpioIp, pigpioPort, armSignalInput):
        # Intialize pigpio
        try: 
            self.pi = pigpio.pi(pigpioIp, pigpioPort) # intalizes self.pi
        except Exception as e:
            print("Failed to connect to pigpio daemon or other Exception: "+ e) #Idk the exact error to look for so this will work
        
        # Initalize arm
        self.pin = armSignalInput
        self.pi.set_mode(self.pin, pigpio.OUTPUT) #listener
        self.pi.set_PWM_frequency(self.pin, 50) # Set frequency to 50Hz 
    
    def close(self):
        '''Sends PWM signals to close arm'''
        self.pi.setServoPulsewidth(self.pin, armCloseWidth)

    def open(self):
        '''Sends PWM signals to open arm'''
        print("opening arm")
        self.pi.setServoPulsewidth(self.pin, armOpenWidth)

    # Neutral signal
    def stop(self):
        '''Neutral signal'''
        self.pi.setServoPulsewidth(self.pin, armNeutralWidth)

if __name__ == "__main__":
    # Testing
    armTest = Arm("192.168.0.2", 8888)
    while True:
        armTest.open()
        time.sleep(2)
        armTest.stop()
        time.sleep(2)
        armTest.close()
        time.sleep(2)
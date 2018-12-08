import socket
import serial
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
# referring to the pins by GPIO numbers
GPIO.setmode(GPIO.BCM)

# define pi GPIO
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

# output pin: Trigger
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
# input pin: Echo
GPIO.setup(GPIO_ECHO,GPIO.IN)
# initialize trigger pin to low
GPIO.output(GPIO_TRIGGER, False)

class ControlStreamingTest(object):
    def __init__(self):
        self.server_socket = socket.socket()
        self.server_socket.bind(('192.168.1.174', 8004))
        self.server_socket.listen(0)
        self.connection, self.client_address = self.server_socket.accept()
        self.ser = serial.Serial('/dev/ttyACM0', 14400, timeout=1)
        self.send_inst = True
        self.streaming()


    def streaming(self):

        try:
            print("Verbindung von: ", self.client_address)

            while True:
                control_data = str(self.connection.recv(1024))
                print("Empfangen: %s" % control_data)
                control_data_int = int(control_data);
                self.ser.write(chr(control_data_int).encode());
        except:
            print("Fehler!")
            self.ser.write(chr(0).encode());
            
        finally:
            self.ser.write(chr(0).encode());
            self.connection.close()
            self.server_socket.close()
            self.send_inst = False
            self.ser.close()

if __name__ == '__main__':
    ControlStreamingTest()

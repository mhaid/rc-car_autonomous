import time
import RPi.GPIO as GPIO
import serial

GPIO.setwarnings(False)

# referring to the pins by GPIO numbers
GPIO.setmode(GPIO.BCM)

# define pi GPIO
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

# define pi GPIO
GPIO_TRIGGER2 = 25
GPIO_ECHO2    = 8

# output pin: Trigger
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
# input pin: Echo
GPIO.setup(GPIO_ECHO,GPIO.IN)
# initialize trigger pin to low
GPIO.output(GPIO_TRIGGER, False)

# output pin: Trigger
GPIO.setup(GPIO_TRIGGER2,GPIO.OUT)
# input pin: Echo
GPIO.setup(GPIO_ECHO2,GPIO.IN)
# initialize trigger pin to low
GPIO.output(GPIO_TRIGGER2, False)


ser = serial.Serial('/dev/ttyACM0', 14400, timeout=1)


def measure():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()

    elapsed = stop-start
    distance = (elapsed * 34300)/2

    return distance

def measure2():
    GPIO.output(GPIO_TRIGGER2, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO2)==0:
        start = time.time()

    while GPIO.input(GPIO_ECHO2)==1:
        stop = time.time()

    

    elapsed = stop-start
    distance = (elapsed * 34300)/2

    return distance

time.sleep(3)


try:
    times = False;
    enabled = True;
    while True:
        distance = measure()
        distance2 = measure2()
        if distance < 40 and times == False:
            times = True;
            print("Warnung: %.2f cm" % distance + " | %.2f cm" % distance2)
        elif distance2 < 40 and times == False:
            times = True;
            print("Warnung: %.2f cm" % distance + " | %.2f cm" % distance2)
        elif distance < 40 or distance2 < 40 and times == True:
            if enabled == True:
                enabled = False;
                if distance < 40:
                    ser.write(chr(15).encode());
                    print("Sending...")
                elif distance2 < 40:
                    ser.write(chr(18).encode());
                    print("Sending...")
            print("Autonomes Stoppen eingeleitet: %.2f cm" % distance + " | %.2f cm" % distance2)
        elif distance < 40 and distance2 < 40 and times == True:
            if enabled == True:
                ser.write(chr(15).encode());
                ser.write(chr(18).encode());
                print("Sending...")
                enabled = False;
            print("Autonomes Stoppen eingeleitet: %.2f cm" % distance + " | %.2f cm" % distance2)
        elif distance > 39 and distance2 >39:
            if times == True:
                times = False;
                enabled = True;
                ser.write(chr(16).encode());
                ser.write(chr(19).encode());
                print("Sending...")
            print("Distanz: %.2f cm" % distance + " | %.2f cm" % distance2)
        time.sleep(0.3)

finally:
    client_socket.close()
    GPIO.cleanup()

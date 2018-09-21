
'''
Search for these patterns on the data from a card

"E?"
"%E?"
";E?"
"E?|"

If one of the sectors has bad data it's likely the card may go soon.
'''



import RPi.GPIO as GPIO
import time

#https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)


'''Tests the lights on startup'''
i = 1
while i < 2 :
    i += 1
    print ("LED on")
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    print ("LED off")
    GPIO.output(17,GPIO.LOW)

    print ("LED on")
    GPIO.output(4,GPIO.HIGH)
    time.sleep(1)
    print ("LED off")
    GPIO.output(4,GPIO.LOW)

''' pin 17 has a red LED for bad reads, pin 4 has a green LED for good reads'''

#import io
#buff = io.StringIO("msg")
#buff.readline()

while True:
    #input ("card")
    card_read = raw_input("input")
    
    if card_read.find(";E?") != -1:
        GPIO.output(17,GPIO.HIGH)
        time.sleep(5)
        print ("Bad Card")
        GPIO.output(17,GPIO.LOW)    
    elif card_read.find("%E?") != -1:
        print ("bad card")
        GPIO.output(17,GPIO.HIGH)
        time.sleep(5)
        print ("Bad Card")
        GPIO.output(17,GPIO.LOW)
    elif card_read.find("E?|") != -1:
        print ("bad card")
        GPIO.output(17,GPIO.HIGH)
        time.sleep(5)
        print ("Bad Card")
        GPIO.output(17,GPIO.LOW)
    else:
        GPIO.output(4,GPIO.HIGH)
        time.sleep(5)
        print ("Less Bad Card")
        GPIO.output(4,GPIO.LOW)

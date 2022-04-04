import RPi.GPIO as GPIO
from random import randint
inA = 25
inB = 5
outS = 16
outC = 21

GPIO.setmode (GPIO.BCM)
GPIO.setup (inA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup (inB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup (outS, GPIO.OUT)
GPIO.setup (outC, GPIO.OUT)

try:
    while True:
        A = GPIO.input (inA)
        B = GPIO.input (inB)

        S = A ^ B
        C = A & B

        GPIO.output (outS, S)
        GPIO.output (outC, C)
except KeyboardInterrupt:
    GPIO.cleanup()
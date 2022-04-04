import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame
from pygame.mixer import Sound

# setup
pygame.init()

GPIO.setmode (GPIO.BCM)

class Simon:
    def __init__(self, debug=False):
        self.debug = debug
        self.leds = [5, 16, 22, 27]
        self.switches = [12, 17, 23, 20]
        self.sounds = [
            Sound ("one.wav"),
            Sound ("two.wav"),
            Sound ("three.wav"),
            Sound ("four.wav")
        ]
        GPIO.setup (self.switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup (self.leds, GPIO.OUT)
        self.create_events ()
        self.seq = [randint (0,3), randint (0,3)]

    def create_events (self):
        for switch in self.switches:
            GPIO.add_event_detect (switch, GPIO.RISING, bouncetime=500)

    def all_on (self):
        GPIO.output (self.leds, True)

    def all_off (self):
        GPIO.output (self.leds, False)

    def lose (self):
        for _ in range (0, 4):
            self.all_on()
            sleep(0.1)
            self.all_off()
            sleep(0.1)

            GPIO.cleanup()
            exit()

    def new_value (self):
        self.seq.append (randint (0, 3))

    def play_seq (self):
        for s in self.seq:
            GPIO.output (self.leds[s], True)
            self.sounds[s].play()
            sleep(1)
            GPIO.output (self.leds[s], False)
            sleep(0.5)

    def user_turn (self):
        user_active = True 
        switches_pressed = 0
        while user_active:
            detec_a_press = False
            for i, switch in enumerate(self.switches):
                if GPIO.event_detected(switch):
                    if self.debug:
                        print (switch)
                    detec_a_press = True
                    button_index = i

            if detec_a_press:
                GPIO.output(self.leds(button_index), True)
                self.sounds[button_index].play()
                sleep (1)
                GPIO.output(self.leds(button_index), False)
                sleep (0.5)

            if button_index != self.seq(switches_pressed):
                self.lose()

            switches_pressed += 1

            if switches_pressed == len (self.seq):
                user_active = False

    def run (self):
        print ("Welcome to Simon!\nPress the buttons to match the pattern you see.\n To quit the game, press Ctrl and c")
        try:
            while True:
                self.new_value()
                #if self.debug:
                    #print (f"seq = {self.seq}")
                self.play_seq()
                self.user_turn

        except KeyboardInterrupt:
            GPIO.cleanup()






s = Simon ()
s.run ()
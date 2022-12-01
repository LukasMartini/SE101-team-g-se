# credit: https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
# import required module

import pygame

import limiter


def playsound():
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        print("rip no button")
        return

    # Import Raspberry Pi GPIO library
    GPIO.setwarnings(False)
    # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)
    # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # Set pin 10 to be an input pin and set initial value to be pulled low (off)

    pygame.mixer.init()
    pygame.mixer.music.load("doorbell.wav")

    while True:
        # Run forever
        if GPIO.input(10) == GPIO.HIGH:
            print("Button was pushed!")  # for playing doorbell.wav file
            ps(1)


@limiter.limit(1)
def ps(_useless_but_required: int):
    pygame.mixer.music.play()

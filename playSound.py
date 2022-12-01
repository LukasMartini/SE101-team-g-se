# credit: https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
# import required module

try:

    import RPi.GPIO as GPIO
    import pygame


    # Import Raspberry Pi GPIO library
    GPIO.setwarnings(False)
    # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)
    # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    while True:
        # Run forever
        if GPIO.input(10) == GPIO.HIGH:
            print("Button was pushed!")  # for playing doorbell.wav file
            pygame.mixer.init()
            pygame.mixer.music.load("doorbell.wav")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
except ImportError:
    print("rip no button")

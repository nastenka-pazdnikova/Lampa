from machine import Pin
from time import sleep

def wait_for_clap(mic):
    while not mic.value():
        sleep(0.01)


mic = Pin(10, Pin.IN, Pin.PULL_UP)
lampa = Pin(11, Pin.OUT)



while True:
    wait_for_clap(mic)
    lampa.high()

    wait_for_clap(mic)
    lampa.low()


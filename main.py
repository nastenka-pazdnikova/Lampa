from machine import Pin
from time import sleep

def wait_for_number_of_claps(mic, claps_count, claps_delay):

    while not mic.value():
        sleep(0.0001)

    sleep(claps_delay)

    wait_timeout = claps_count * claps_delay

    while not mic.value() and wait_timeout > 0:
        sleep(0.001)
        wait_timeout = wait_timeout - 0.001

    return wait_timeout > 0


mic = Pin(10, Pin.IN, Pin.PULL_UP)
lampa = Pin(11, Pin.OUT)



while True:
    while not wait_for_number_of_claps(mic, 2, 0.2):
        pass

    lampa.high()
    sleep(0.5)

    while not wait_for_number_of_claps(mic, 2, 0.2):
        pass


    lampa.low()
    sleep(0.5)

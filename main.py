from machine import Pin
from time import sleep

def wait_for_number_of_claps(mic, claps_count, claps_delay):

    for i in range(claps_count):

        wait_timeout = claps_delay
        while wait_timeout > 0:

            if mic.value():
                break

            sleep(0.001)
            wait_timeout = wait_timeout - 0.001

        if not wait_timeout > 0:
            return False

        print(f"cought clap {i + 1}")
        sleep(claps_delay)

    print(f"catch claps {claps_count}")

    return True


mic = Pin(10, Pin.IN, Pin.PULL_UP)
lampa = Pin(11, Pin.OUT)



while True:
    while not wait_for_number_of_claps(mic, 3, 0.2):
        pass

    lampa.high()
    sleep(0.5)

    while not wait_for_number_of_claps(mic, 2, 0.2):
        pass


    lampa.low()
    sleep(0.5)

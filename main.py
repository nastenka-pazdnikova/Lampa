from time import sleep

from machine import Pin


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


def count_number_of_claps(mic, claps_delay):
    while not mic.value():
        sleep(0.001)

    for delay in claps_delay:
        sleep(delay)

        wait_timeout = 0.2
        while wait_timeout > 0:

            if mic.value():
                break

            sleep(0.001)
            wait_timeout = wait_timeout - 0.001

        if not wait_timeout > 0:
            return False

        print(f"cought clap {delay}")

    print(f"catch claps {claps_delay}")

    return True


mic = Pin(10, Pin.IN, Pin.PULL_UP)
lampa = Pin(11, Pin.OUT)


def detect_sequence_of_claps(mic, claps_delay):
    while not mic.value():
        sleep(0.001)

    while True:
        sleep(0.1)
        delay_current = 0.1

        while not mic.value():
            sleep(0.001)
            delay_current = delay_current + 0.001

            if delay_current > 2:
                return

        print(delay_current)
        claps_delay.append(delay_current)





def exact_number_of_claps():
    while True:
        while not wait_for_number_of_claps(mic, 3, 0.2):
            pass

        lampa.high()
        sleep(0.5)

        while not wait_for_number_of_claps(mic, 2, 0.2):
            pass

        lampa.low()
        sleep(0.5)


def dynamic_claps():
    while True:

        while not count_number_of_claps(mic, [0.2, 0.5]):
            pass

        lampa.high()
        sleep(0.5)

        while not count_number_of_claps(mic, [0.5, 0.2]):
            pass

        lampa.low()
        sleep(0.5)


def detect_claps():
    while True:

        claps = []

        detect_sequence_of_claps(mic, claps)
        print(f"cought {len(claps)} : {claps}")



detect_claps()

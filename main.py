# Metronome (4/4)

from time import sleep
from winsound import Beep


def metronome(bpm):
    """Metronome that asks the user for the BPM (Beats-Per-Minute) and prints 4-count and windows audio beep.

    Args:
        bpm (int): Beats-Per-Minute.

    """
    count = 0

    while count <= 4:
        sleep(float(60 / bpm - 0.1))
        count += 1
        print(count)
        Beep(440, 100)

        if count == 4:
            count = 0

metronome(int(input("Enter BPM: ")))

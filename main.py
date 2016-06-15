# Metronome - Johnathon Kwisses (Kwistech)
from tkinter import *
from winsound import Beep


class Metronome:
    """Create Metronome app with class instance."""

    def __init__(self, root, beats):
        """Initiate default values for class and call interface().

        Args:
            root (tkinter.Tk): Main class instance for tkinter.
            beats (list): Contains time signatures for metronome.
        """
        self.root = root
        self.beats = beats

        self.start = False
        self.bpm = 0
        self.count = 0
        self.beat = 0
        self.time = 0

        self.var = StringVar()
        self.var.set(self.count)

        self.interface()

    def interface(self):
        """Set interface for Metronome app."""
        frame = Frame()
        frame.pack()

        entry = Entry(frame, width=8, justify="center")
        entry.insert(0, "60")
        entry.grid(row=0, column=0, padx=5, sticky="E")

        spinbox = Spinbox(frame, width=5, values=self.beats, wrap=True)
        spinbox.grid(row=0, column=1, sticky="E")

        label_bpm = Label(frame, text="BPM:")
        label_bpm.grid(row=0, column=0, sticky="W")

        label_time = Label(frame, text="Time:")
        label_time.grid(row=0, column=1, padx=5, sticky="W")

        label_count = Label(frame, textvariable=self.var, font=("Arial", 30))
        label_count.grid(row=1, column=0, columnspan=2)

        button_start = Button(frame, text="Start", width=10, height=2,
                              command=lambda: self.start_counter(entry,
                                                                 spinbox))
        button_start.grid(row=2, column=0, padx=10, sticky="W")

        button_stop = Button(frame, text="Stop", width=10, height=2,
                             command=lambda: self.stop_counter())
        button_stop.grid(row=2, column=1, padx=10, sticky="E")

    def start_counter(self, entry, spinbox):
        """Start counter if self.start is False (prevents multiple starts).

        Args:
            entry (tkinter.Entry): tkinter Entry widget for app.
            spinbox (tkinter.Spinbox): tkinter Spinbox widget for app.

        Raises:
            ValueError: if bpm field (self.bpm) on tkinter app is left blank.
        """
        if not self.start:
            try:
                self.bpm = int(entry.get())
            except ValueError:
                self.bpm = 60
            else:
                if self.bpm > 300:  # Limits BPM
                    self.bpm = 300

            self.time = int((60 / self.bpm - 0.1) * 1000)  # Math for delay

            self.start = True
            self.counter(spinbox)

    def stop_counter(self):
        """Stop counter by setting self.start to False."""
        self.start = False

    def counter(self, spinbox):
        """Control counter display and audio with calculated time delay.

        Args:
            spinbox (tkinter.Spinbox): tkinter Spinbox widget to get beat.
        """
        if self.start:
            self.beat = int(spinbox.get()[0])
            self.count += 1
            self.var.set(self.count)

            if self.count == 1:
                Beep(880, 100)
            elif self.count >= self.beat:
                self.count = 0
                Beep(440, 100)
            else:
                Beep(440, 100)

            # Calls this method after a certain amount of time (self.time).
            self.root.after(self.time, lambda: self.counter(spinbox))


def main():
    """Call Metronome class instance with tkinter root class settings."""
    root = Tk()
    root.title("Metronome")

    beats = ["4/4", "2/4", "3/4"]
    Metronome(root, beats)

    root.mainloop()

if __name__ == "__main__":
    main()

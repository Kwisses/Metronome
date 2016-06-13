# Metronome - Johnathon Kwisses (Kwistech)
from tkinter import *
from winsound import Beep


class Metronome:

    def __init__(self, root, beats):
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
        if not self.start:
            try:
                self.bpm = int(entry.get())
            except ValueError:
                self.bpm = 60
            else:
                if self.bpm > 300:
                    self.bpm = 300

            self.time = int((60 / self.bpm - 0.1) * 1000)
            self.start = True
            self.counter(spinbox)

    def stop_counter(self):
        self.start = False

    def counter(self, spinbox):
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

            self.root.after(self.time, lambda: self.counter(spinbox))


def main():
    root = Tk()
    root.title("Metronome")

    beats = ["4/4", "2/4", "3/4"]
    Metronome(root, beats)

    root.mainloop()

if __name__ == "__main__":
    main()

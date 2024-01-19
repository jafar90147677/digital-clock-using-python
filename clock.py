import time
from tkinter import *

class Clock:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Clock")
        self.parent.geometry("300x200")
        self.time = time.strftime("%H:%M:%S")
        self.time_label = Label(self.parent, text=self.time, font=("times new roman", 20))
        self.time_label.pack(fill=BOTH, expand=1)
        self.update_time()

    def update_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.time_label.config(text=self.time)
        self.time_label.after(1000, self.update_time)

if __name__ == "__main__":
    root = Tk()
    clock = Clock(root)
    root.mainloop()
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class ClockApp:
    def __init__(self, master):
        self.master = master
        master.title("Rooster watch")
        master.minsize(220, 150)

        self.time = datetime.now().replace(microsecond=0)
        self.current_color = "green"

        self.label_font_size = 48
        self.button_font_size = 16

        style = ttk.Style()
        style.configure("TButton", padding=5)  # Buttons style
        style.configure("TFrame", padding=0)

        self.label = tk.Label(master, text="", font=("Arial", self.label_font_size, "bold"), fg="black", bg=self.current_color)
        self.label.pack(expand=True, fill="both", padx=5, pady=5)  # Edges

        button_frame = ttk.Frame(master)
        button_frame.pack(fill="x", padx=5, pady=5)

        self.add_button = ttk.Button(button_frame, text="+1 second", command=self.add_second)
        self.add_button.pack(side="left", expand=True, fill="both", padx=5)

        self.subtract_button = ttk.Button(button_frame, text="-1 second", command=self.subtract_second)
        self.subtract_button.pack(side="right", expand=True, fill="both", padx=5)

        self.label.bind("<Configure>", self.resize_font)

        self.update_clock()

    def add_second(self):
        self.time += timedelta(seconds=1)

    def subtract_second(self):
        self.time -= timedelta(seconds=1)

    def update_clock(self):
        self.label.config(text=self.time.strftime("%H:%M:%S"))
        self.update_background()
        self.time += timedelta(seconds=1)
        self.master.after(1000, self.update_clock)

    def update_background(self):
        minute = self.time.minute
        second = self.time.second

        if minute in [8, 23, 38, 53] and second == 0 and self.current_color != "red":
            self.current_color = "red"
            self.label.config(bg="red")
        elif minute in [9, 24, 39, 54] and second == 40 and self.current_color != "#4B0082":
            self.current_color = "#4B0082"
            self.label.config(bg="#4B0082")
        elif minute in [10, 25, 40, 55] and second == 0 and self.current_color != "green":
            self.current_color = "green"
            self.label.config(bg="green")

    def resize_font(self, event):
        new_size = min(event.height, event.width // 6)
        new_size = max(12, new_size)
        self.label.config(font=("Arial", new_size, "bold"))

root = tk.Tk()
app = ClockApp(root)
root.mainloop()

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class CreateProfileFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.Title = tk.Label(self, text="Create User Profile", font="times 20 bold")
        self.Title.grid(row=0, column=3)

        self.user_image = ImageTk.PhotoImage(Image.open("userIcon.png").resize((80, 80)))
        self.panel = tk.Label(self, image=self.user_image)
        self.panel.grid(row=1, column=3)

        self.wake_up_hour = ttk.Label(self, text="Wake-up Hour", style="BW.TLabel")
        self.wake_up_hour.grid(row=2, column=2)

        self.sleep_hour = ttk.Label(self, text="Sleep Hour", style="BW.TLabel")
        self.sleep_hour.grid(row=3, column=2)

        self.timer = ttk.Label(self, text="Timer", style="BW.TLabel")
        self.timer.grid(row=4, column=2)

        self.lights_color = ttk.Label(self, text="Lights color", style="BW.TLabel")
        self.lights_color.grid(row=5, column=2)

        self.lights_intensity = ttk.Label(self, text="Lights intensity", style="BW.TLabel")
        self.lights_intensity.grid(row=6, column=2)

        # values of fields
        self.wake_up_hour_value = tk.StringVar
        self.sleep_hour_value = tk.StringVar
        self.timer_value = tk.DoubleVar
        self.lights_color_value = tk.StringVar
        self.lights_intensity_value = tk.IntVar
        self.same_as_outside_lights_value = tk.BooleanVar()

        # boxes
        self.wake_up_hour_box = tk.Entry(self, textvariable=self.wake_up_hour_value)
        self.sleep_hour_box = tk.Entry(self, textvariable=self.sleep_hour_value)
        self.timer_box = tk.Entry(self, textvariable=self.timer_value)
        self.lights_color_box = tk.Entry(self, textvariable=self.lights_color_value)
        self.lights_intensity_box = tk.Entry(self, textvariable=self.lights_intensity_value)

        self.wake_up_hour_box.grid(row=2, column=3)
        self.sleep_hour_box.grid(row=3, column=3)
        self.timer_box.grid(row=4, column=3)
        self.lights_color_box.grid(row=5, column=3)
        self.lights_intensity_box.grid(row=6, column=3)

        self.check_box = tk.Checkbutton( self, text="Same as outside lights", variable=self.same_as_outside_lights_value,
                                        font="Cambria")
        self.check_box.grid(row=7, column=2)

        self.B = tk.Button(self, text="Submit", bg='light blue', font=('Times New Roman', 15, 'bold'), width='12')
        self.B.grid(row=8, column=3)

        style_object = ttk.Style()
        style_object.configure("BW.TLabel", font=('Cambria', 12))



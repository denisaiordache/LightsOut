import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class CreateProfileFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.Title = tk.Label(self, text="Create User Profile", font=("Microsoft JhengHei UI",22,"bold"))
        self.Title.grid(row=0, column=1, columnspan=2,pady=(10, 65))

        self.user_image = ImageTk.PhotoImage(Image.open("Assets/.png").resize((140, 140)))
        self.panel = tk.Label(self, image=self.user_image)
        self.panel.grid(row=1, column=2,pady=(10, 15))

        self.wake_up_hour = ttk.Label(self, text="Wake-up Hour", style="BW.TLabel")
        self.wake_up_hour.grid(row=2, column=1)

        self.sleep_hour = ttk.Label(self, text="Sleep Hour", style="BW.TLabel")
        self.sleep_hour.grid(row=3, column=1)

        self.timer = ttk.Label(self, text="Timer", style="BW.TLabel")
        self.timer.grid(row=4, column=1)

        self.lights_color = ttk.Label(self, text="Lights color", style="BW.TLabel")
        self.lights_color.grid(row=5, column=1)

        self.lights_intensity = ttk.Label(self, text="Lights intensity", style="BW.TLabel")
        self.lights_intensity.grid(row=6, column=1)

        # values of fields
        self.wake_up_hour_value = tk.StringVar
        self.sleep_hour_value = tk.StringVar
        self.timer_value = tk.DoubleVar
        self.lights_color_value = tk.StringVar
        self.lights_intensity_value = tk.IntVar
        self.same_as_outside_lights_value = tk.BooleanVar()

        # boxes
        self.wake_up_hour_box = tk.Entry(self, textvariable=self.wake_up_hour_value, justify="center", width=25)
        self.sleep_hour_box = tk.Entry(self, textvariable=self.sleep_hour_value, justify="center", width=25)
        self.timer_box = tk.Entry(self, textvariable=self.timer_value, justify="center", width=25)
        self.lights_color_box = tk.Entry(self, textvariable=self.lights_color_value, justify="center", width=25)
        self.lights_intensity_box = tk.Entry(self, textvariable=self.lights_intensity_value, justify="center", width=25)

        self.wake_up_hour_box.grid(row=2, column=2, pady=(7,7), ipady=7, ipadx=12)
        self.sleep_hour_box.grid(row=3, column=2, pady=(7,7), ipady=7, ipadx=12)
        self.timer_box.grid(row=4, column=2, pady=(7,7), ipady=7, ipadx=12)
        self.lights_color_box.grid(row=5, column=2, pady=(7,7), ipady=7, ipadx=12)
        self.lights_intensity_box.grid(row=6, column=2, pady=(7,7), ipady=7, ipadx=12)

        self.check_box = tk.Checkbutton( self, text="Same as outside lights", variable=self.same_as_outside_lights_value,
                                        font="Cambria")
        self.check_box.grid(row=7, column=1)

        self.B = tk.Button(self, text="Submit", bg='#28a745',activebackground="#25873c",fg="white",activeforeground="white", font=('Microsoft JhengHei UI', 13, 'bold'), width=19, relief="flat")
        self.B.grid(row=8, column=2, pady=(30,0))

        style_object = ttk.Style()
        style_object.configure("BW.TLabel", font=('Cambria', 12))



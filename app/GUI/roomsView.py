import tkinter as tk
from tkinter import ttk





class App(tk.Tk):
    def __init__(self):
        super().__init__()





        self.geometry("840x700")
        self.title('Rooms')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)
        self.option_add("*Font", "\"Microsoft JhengHei UI\" 10")
        self.titleLabel = tk.Label(text='My Rooms', font=("Microsoft JhengHei UI", 40, "bold")  )
        self.titleLabel.grid(column=1, row=0, pady=(10, 10))

        self.rooms = []
        for i in range(2):
            self.rooms.append(None)
            self.rooms[i] = RoomFrame(self, i+1)


class RoomFrame(ttk.Frame):
    def __init__(self, container, row):
        super().__init__(container)

        s = ttk.Style()
        s.configure('RoomFrame.TFrame', background='green')
        self.configure(style='RoomFrame.TFrame', width=900)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # numele camerei

        self.title = ttk.Label(self, text='Livingroom', font=("Microsoft JhengHei UI", 20, "bold"))
        self.title.grid(columnspan=2, row=0, padx=(20,20),pady=(0,20))

        # lista surselor de lumina din camera

        self.lightsList = []

        vars = []
        for i in range(10):
            var = tk.IntVar()
            vars.append(var)
            self.lightsList.append(tk.Checkbutton(self, text="Light " + str(i + 1), variable=var))
            self.lightsList[i].grid(column=0, row=i+1, sticky='W')

        # butoane

        self.switchAllLightsOnButton = ttk.Button(self, text='Switch all lights on')
        self.switchAllLightsOnButton.grid(column=3, row=1, padx=(100,0))

        self.switchAllLightsOffButton = ttk.Button(self, text='Switch all lights off')
        self.switchAllLightsOffButton.grid(column=3, row=2, padx=(100,0))

        self.grid(column=1, row=row, padx=20, pady=20)
        self['padding'] = (100, 50)


if __name__ == "__main__":
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        app = App()
        app.mainloop()

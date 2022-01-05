import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class ScrollableFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        s = ttk.Style()
        s.configure('Scroll.TFrame') #, background='#FAE3E3')
        self.configure(style='Scroll.TFrame')

        self.canvas = tk.Canvas( width=1055) # bg="#FAE3E3",
        self.canvas.pack(side='left', fill="both", expand=1)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.scrollbar = ttk.Scrollbar(
            self,
            orient='vertical',
            command=self.canvas.yview
        )
        self.scrollbar.pack(side='right', fill='y')
        self.canvas['yscrollcommand'] = self.scrollbar.set

        # show wanted frame

        self.second_frame = MyRoomsFrame(self.canvas)
        self.canvas.create_window((100, 0), window=self.second_frame, anchor='nw')

    def destroy(self) -> None:
        super().destroy()
        self.canvas.destroy()
        self.scrollbar.destroy()
        self.second_frame.destroy()


class MyRoomsFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        s = ttk.Style()
        s.configure('MyRoomsFrame.TFrame') #, background='#FAE3E3')
        self.configure(style='MyRoomsFrame.TFrame')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        self.titleLabel = tk.Label(self, text='My Rooms', # bg="#FAE3E3",
                                   font=("Microsoft JhengHei UI", 22, 'bold'), fg="black")
        self.titleLabel.grid(column=1, row=0, pady=(10, 10))

        self.rooms = []
        for i in range(2):
            self.rooms.append(None)
            self.rooms[i] = RoomFrame(self, i + 1)



class RoomFrame(ttk.Frame):
    def __init__(self, container, index):
        super().__init__(container)

        s = ttk.Style()
        s.configure('RoomFrame.TFrame', background='white')
        self.configure(style='RoomFrame.TFrame')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # numele camerei

        s.configure(style='Title.TLabel', background="white", foreground = "grey")
        self.title = ttk.Label(self, text='Livingroom', style='Title.TLabel', wraplength=700,
                               font=("Microsoft JhengHei UI", 16, "bold"))
        self.title.grid(columnspan=2, row=0, padx=(20, 20), pady=(0, 20),sticky="w")

        # lista surselor de lumina din camera

        self.lightsList = []

        self.vars = []
        for i in range(10):
            var = tk.IntVar(value=0)
            self.vars.append(var)
            self.lightsList.append(tk.Checkbutton(self, text="Light " + str(i + 1),fg="black", bg='white',activebackground="grey", variable=var, onvalue=1, offvalue=0, command=self.printLightsState))
            self.lightsList[i].grid(column=0, row=i + 1, sticky='W', pady=5)

        # butoane

        self.photoOn = ImageTk.PhotoImage(Image.open(r"Assets/LightOn.png").resize((20, 20)))

        self.switchAllLightsOnButton = tk.Button(self, text='All lights on', background="#d8ab3a", image=self.photoOn,relief='flat',
                                                 activebackground="#aa872e", compound="left", command=self.switchOnAllLights)
        self.switchAllLightsOnButton.grid(column=1, row=1, padx=(400, 0), ipadx=5, ipady=5)

        self.photoOff = ImageTk.PhotoImage(Image.open(r"Assets/LightOff.png").resize((20, 20)))

        self.switchAllLightsOffButton = tk.Button(self, text='All lights off', background="#014372",relief='flat',
                                                  activebackground="#003459",image=self.photoOff, compound="left", command=self.switchOffAllLights)
        self.switchAllLightsOffButton.grid(column=1, row=2, padx=(400, 0),pady=(5,0), ipadx=5, ipady=5)

        self.grid(column=1, row=index, padx=20, pady=20)
        self['padding'] = (100, 30)

    def switchOffAllLights(self):
        for var in self.vars:
            var.set(0)

    def switchOnAllLights(self):
        for var in self.vars:
            var.set(1)

    def printLightsState(self):
        for i in range(len(self.vars)):
            if self.vars[i].get() == 0:
                print(f'Light {i+1} is off')
            else:
                print(f'Light {i+1} is on')
        print('\n')
import tkinter as tk
from roomsView import ScrollableFrame
from createProfileFrame import CreateProfileFrame
from PIL import ImageTk, Image


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1400x840")
        self.resizable(False, False)
        self.config(bg="#FAE3E3")
        self.title('LightsOut')
        self.option_add("*Font", "\"Microsoft JhengHei UI\" 10")

        # Menu
        self.menu = tk.LabelFrame(bg='red', borderwidth=0)
        self.menu.pack(side='left', fill='y')

        self.bulbIcon = ImageTk.PhotoImage(Image.open("Assets/icon.png").resize((200, 200)))
        self.panel = tk.Label(self.menu, image=self.bulbIcon, background='red')
        self.panel.pack(side='bottom')

        self.menuLabel = tk.Label(self.menu, text='Menu', bg='pink', font=("Microsoft JhengHei UI", 20, 'bold'))
        self.menuLabel.pack(ipadx=5, ipady=5, fill='x')

        # Button for rooms
        self.roomsButton = tk.Button(self.menu, text='My Rooms', background="#f9dd52",
                                     relief='flat',
                                     activebackground="#fcd200", compound="left", width=30, command=self.showMyRooms)

        self.roomsButton.pack(ipadx=5, ipady=5, fill='x')

        # Button for create profile
        self.roomsButton = tk.Button(self.menu, text='Create Profile', background="#f9dd52",
                                     relief='flat',
                                     activebackground="#fcd200", compound="left", width=30, command=self.showCreateProfile)

        self.roomsButton.pack(ipadx=5, ipady=5, fill='x')

        # starting frame
        self.frame = CreateProfileFrame(self)
        self.frame.pack(side= 'right',fill="both", expand=1)

    def showMyRooms(self):
        self.frame.destroy()
        self.frame = ScrollableFrame(self)
        self.frame.pack(side= 'right',fill="both", expand=1)

    def showCreateProfile(self):
        self.frame.destroy()
        self.frame = CreateProfileFrame(self)
        self.frame.pack(side= 'right',fill="both", expand=1)

if __name__ == "__main__":
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        app = App()
        app.mainloop()

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
        self.menu = tk.LabelFrame(bg='#003459', borderwidth=0)
        self.menu.pack(side='left', fill='y')

        self.bulbIcon = ImageTk.PhotoImage(Image.open("Assets/icon.png").resize((200, 200)))
        self.menuIcon = ImageTk.PhotoImage(Image.open("Assets/menuIcon.png").resize((36, 36)))
        self.panel = tk.Label(self.menu, image=self.bulbIcon, background='#003459')
        self.panel.pack(side='bottom')

        self.menuLabel = tk.Label(self.menu, text='Menu',compound="left", bg='#003459', fg="#d8ab3a", font=("Microsoft JhengHei UI", 15, 'bold'),anchor='w')
        self.menuLabel.pack(padx=5,ipadx=10, ipady=10, fill='x')

        # Button for create profile
        self.roomsButton = tk.Button(self.menu, text='Create Profile', background="#d8ab3a",
                                     relief='flat',
                                     activebackground="#aa872e", compound="left", width=30,
                                     command=self.showCreateProfile)

        self.roomsButton.pack(pady=10,ipadx=5, ipady=5, fill='x')

        # Button for rooms
        self.roomsButton = tk.Button(self.menu, text='My Rooms', background="#d8ab3a",
                                     relief='flat',
                                     activebackground="#aa872e", compound="left", width=30, command=self.showMyRooms)

        self.roomsButton.pack(ipadx=5, ipady=5, fill='x')



        # starting frame
        self.frame = ScrollableFrame(self)
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

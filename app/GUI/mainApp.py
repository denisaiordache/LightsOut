import tkinter as tk
from roomsView import ScrollableFrame
from createProfileFrame import CreateProfileFrame
from updateProfile import UpdateProfileFrame
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
        self.refreshIcon = ImageTk.PhotoImage(Image.open("Assets/refresh.png").resize((20, 20)))
        self.panel = tk.Label(self.menu, image=self.bulbIcon, background='#003459')
        self.panel.pack(side='bottom')
        self.buttons = tk.Label(self.menu, background='#003459')
        self.buttons.columnconfigure(0, weight=1)
        self.buttons.columnconfigure(1, weight=1)
        self.buttons.pack()

        self.menuLabel = tk.Label(self.buttons, text='Menu',image=self.menuIcon,compound="left", bg='#003459', fg="#d8ab3a", font=("Microsoft JhengHei UI", 15, 'bold'),anchor='w')
        self.menuLabel.grid(column=0,row=0, padx=5,ipadx=10, ipady=10,sticky='w')

        # Button for create profile
        self.refreshButton = tk.Button(self.buttons, image=self.refreshIcon, background="#003459",
                                     relief='flat',
                                     activebackground="#aa872e", compound="left", width=20,
                                     command=self.refresh)
        self.refreshButton.grid(column=1,row=0,ipady=5,ipadx=5,padx=(0,5),sticky='e')

        # Button for create profile
        self.roomsButton = tk.Button(self.buttons, text='Create Profile', background="#d8ab3a",
                                     relief='flat',
                                     activebackground="#aa872e", compound="left", width=30,
                                     command=self.showCreateProfile)

        self.roomsButton.grid(column=0,row=1,columnspan=2,pady=5,ipadx=5, ipady=5)

        # Button for rooms
        self.roomsButton = tk.Button(self.buttons, text='My Rooms', background="#d8ab3a",
                                     relief='flat',
                                     activebackground="#aa872e", compound="left", width=30, command=self.showMyRooms)

        self.roomsButton.grid(column=0,row=2,columnspan=2,pady=5,ipadx=5, ipady=5)

        #Button for view/update profile
        self.profileButton = tk.Button(self.buttons, text='My Profile', background="#d8ab3a",
                                     relief='flat',
                                     activebackground="#aa872e", compound="left", width=30, command=self.showUpdateProfile)

        self.profileButton.grid(column=0,row=3,columnspan=2,pady=5,ipadx=5, ipady=5)


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

    def showUpdateProfile(self):
        self.frame.destroy()
        self.frame = UpdateProfileFrame(self)
        self.frame.pack(side= 'right',fill="both", expand=1)

    def refresh(self):
        name = self.frame.__class__.__name__

        self.frame.destroy()

        if name == 'ScrollableFrame':
            self.frame = ScrollableFrame(self)
        elif name == 'UpdateProfileFrame':
            self.frame = UpdateProfileFrame(self)
        elif name == 'CreateProfileFrame':
            self.frame = CreateProfileFrame(self)

        self.frame.pack(side= 'right',fill="both", expand=1)

if __name__ == "__main__":
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        app = App()
        app.mainloop()

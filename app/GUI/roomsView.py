import tkinter as tk
from tkinter import ttk

import requests
from PIL import ImageTk, Image
from ttkwidgets import TickScale
from tkinter import colorchooser


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
        self.cont = container
        s = ttk.Style()
        s.configure('MyRoomsFrame.TFrame') #, background='#FAE3E3')
        self.configure(style='MyRoomsFrame.TFrame')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        self.titleLabel = tk.Label(self, text='My Rooms', # bg="#FAE3E3",
                                   font=("Microsoft JhengHei UI", 22, 'bold'), fg="black")
        self.titleLabel.grid(column=1, row=0, pady=(10, 10))

        #add room elements
        self.roomName = tk.Label(self, text="Add room",font=("Microsoft JhengHei UI", 15, 'bold'), fg="black")
        self.roomName.grid(column=1,row=1,pady=(10,10))

        self.room_value = tk.StringVar()

        self.roomBox = tk.Entry(self, justify="center",textvariable=self.room_value, width=25)
        self.roomBox.grid(column=1,row=2,pady=(10,10))

        self.addIcon = ImageTk.PhotoImage(Image.open("Assets/plus.jpg").resize((20,20)))
        self.addButton = tk.Button(self,image=self.addIcon,relief='flat',command=self.createRoom)
        self.addButton.grid(column=1,row=2,pady=(10,10),padx=(250,0))

        res = self.getCurrentUser()
        self.username = res['profile_name']

        self.rooms = []
        self.roomsData = res['rooms']
        for i in range(len(self.roomsData)):
            self.rooms.append(None)
            self.rooms[i] = RoomFrame(self, i + 3, self.roomsData[i])



    def getCurrentUser(self):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.get('http://127.0.0.1:5000/user_profile/-1', json={}, headers=headers)
        print(response, response.content)
        users = response.json()['user_profiles']

        for user in users:
            if user['is_active'] == True:
                return user





    def createRoom(self):
        roomName = self.roomBox.get()

        data = {
            'id':None,
            'name':roomName,
            'profile_name':self.username
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post('http://127.0.0.1:5000/room/1', json=data, headers=headers)
        print(response, response.content)
        self.room_value.set("")

    def get_user(self,username):
        response = requests.get(url='http://127.0.0.1:5000/user_profile/' + str(username))
        return response.json()


class RoomFrame(ttk.Frame):
    def __init__(self, container, index, room):
        super().__init__(container)
        self.room = room
        s = ttk.Style()
        s.configure('RoomFrame.TFrame', background='white')
        self.configure(style='RoomFrame.TFrame')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # numele camerei

        s.configure(style='Title.TLabel', background="white", foreground = "grey")
        self.title = ttk.Label(self, text=room['name'], style='Title.TLabel', wraplength=700,
                               font=("Microsoft JhengHei UI", 16, "bold"))
        self.title.grid(columnspan=2, row=0, padx=(20, 20), pady=(0, 20),sticky="w")

        # lista surselor de lumina din camera

        self.lightsList = self.room['lights']
        self.lightCheckBoxes = []
        self.vars = []
        self.deleteButtons=[]
        self.binIcon = ImageTk.PhotoImage(Image.open("Assets/binIcon.png").resize((20, 20)))
        for i in range(len(self.lightsList)):
            var = tk.IntVar(value=self.lightsList[i]['on'])
            self.vars.append(var)
            self.lightCheckBoxes.append(tk.Checkbutton(self, text=self.lightsList[i]['name'],fg="black", bg='white',activebackground="grey",
                                                  variable=var, onvalue=1, offvalue=0, command=self.printLightsState))
            self.lightCheckBoxes[i].grid(column=0, row=i + 1, sticky='W', pady=5)
            self.deleteButtons.append(tk.Button(self,image=self.binIcon,text=str(i),bg='white',relief='flat',command= lambda m=str(i):self.deleteLight(int(m))))
            self.deleteButtons[i].grid(column=0, row=i + 1, sticky='E', pady=5, padx=(100,0))
        # butoane

        self.photoOn = ImageTk.PhotoImage(Image.open(r"Assets/LightOn.png").resize((20, 20)))

        self.switchAllLightsOnButton = tk.Button(self, text='All lights on', background="#d8ab3a", image=self.photoOn,relief='flat',
                                                 activebackground="#aa872e", compound="left", command=self.switchOnAllLights)
        self.switchAllLightsOnButton.grid(column=1, row=1, padx=(100, 0), ipadx=5, ipady=5)

        self.photoOff = ImageTk.PhotoImage(Image.open(r"Assets/LightOff.png").resize((20, 20)))

        self.switchAllLightsOffButton = tk.Button(self, text='All lights off', background="#014372",relief='flat',
                                                  activebackground="#003459",image=self.photoOff, compound="left", command=self.switchOffAllLights)
        self.switchAllLightsOffButton.grid(column=1, row=1, padx=(400, 0), ipadx=5, ipady=5)

        self.grid(column=1, row=index, padx=20, pady=20)
        self['padding'] = (100, 30)

        #text for slider
        self.lightsIntensity = tk.Label(self, text="Lights intensity", background="white")
        self.lightsIntensity.grid(column=1, row=3, padx=(230, 0), ipadx=5)


        #slider
        s.configure('custom.Horizontal.TScale', background='white', foreground='grey',
                    troughcolor='#73B5FA',)
        self.scale = TickScale(self, from_=0, to=100, tickinterval=100, orient="horizontal", length=280,
                               style='custom.Horizontal.TScale', command=self.updateLights)

        self.scale.grid(column=1, row=4, padx =(250,0),ipadx=5, rowspan=3)

        #choose color button
        self.colorChooser = ImageTk.PhotoImage(Image.open(r"Assets/color-picker.jpg").resize((40, 40)))
        self.selectColorButton = tk.Button(self, text='Select color', background="#F5F5F5", relief='flat',
                                                  activebackground="#E8E8E8", image=self.colorChooser, compound="left",
                                                  command=self.chooseColor)
        self.selectColorButton.grid(column=1, row=7, padx=(105, 0), ipadx=5, ipady=5, rowspan=2)

        if len(self.lightsList) > 0:
            self.color_code = self.lightsList[0]['color']
            self.scale.set(self.lightsList[0]['intensity'])
        else:
            self.color_code = '#FFFF00'

        #label for displaying color
        self.choosedColor = tk.Label(self, background = self.color_code, width = 9, height = 2)
        self.choosedColor.grid(column =1, row=7, padx=(450, 0), ipadx=5, ipady=5,rowspan=2)


        #Add light form
        self.lightName = tk.Label(self, text="Add light",bg='white', fg="black")
        self.lightName.grid(column=1,row=9,pady=(10,10),padx=(250,0))

        self.light_val = tk.StringVar()

        self.lightBox = tk.Entry(self, justify="center", width=25, background='lightgrey', textvariable=self.light_val)
        self.lightBox.grid(column=1,row=10,pady=(10,10),padx=(230,0),ipadx=5, ipady=5,rowspan=2)

        self.addIcon = ImageTk.PhotoImage(Image.open("Assets/plus.jpg").resize((20,20)))
        self.addButton = tk.Button(self,image=self.addIcon,relief='flat',background='white', command=self.createLight)
        self.addButton.grid(column=1,row=10,pady=(10,10),padx=(520,0),ipady=5,rowspan=2)

        self.addButton = tk.Button(self, text="Delete room",image=self.binIcon, compound='left', relief='flat',bg='#9e0027',fg='white', activebackground='#9e0027',
                                   command=self.deleteRoom)
        self.addButton.grid(column=1, row=12, pady=(70, 10), padx=(420, 0), ipady=5,ipadx=5, rowspan=2)


    def chooseColor(self):
        self.color_code = colorchooser.askcolor(title="Choose color")[1]
        self.choosedColor.config(bg=self.color_code)
        self.updateLights("")


    def switchOffAllLights(self):
        for var in self.vars:
            var.set(0)
        self.scale.set(0)
        self.updateLights("")

    def switchOnAllLights(self):
        for var in self.vars:
            var.set(1)
        self.scale.set(50)
        self.updateLights("")

    def printLightsState(self):
        for i in range(len(self.vars)):
            if self.vars[i].get() == 0:
                print(f'Light {i+1} is off')
            else:
                print(f'Light {i+1} is on')
        print('\n')
        self.updateLights("")



    def createLight(self):
        data = {
            "id":None,
            "name": self.lightBox.get(),
            "room_id": self.room["id"],
            "on": None,
            "color": str(self.color_code),
            "intensity": self.scale.get()
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post('http://127.0.0.1:5000/light/1', json=data, headers=headers)
        print(response,response.content)
        self.light_val.set("")

    def updateLights(self,event):

        for i in range(len(self.lightsList)):
            self.lightsList[i]['on'] = self.vars[i].get()
            self.lightsList[i]['color'] = self.color_code
            self.lightsList[i]['intensity'] = self.scale.get()

            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            response = requests.put('http://127.0.0.1:5000/light/'+str(self.lightsList[i]['id']), json=self.lightsList[i], headers=headers)
            print(response, response.content)

    def deleteLight(self,i):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.delete('http://127.0.0.1:5000/light/' + str(self.lightsList[i]['id']), json=self.lightsList[i], headers=headers)
        print(response, response.content)

    def deleteRoom(self):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.delete('http://127.0.0.1:5000/room/' + str(self.room['id']),
                                   json=self.room, headers=headers)
        print(response, response.content)




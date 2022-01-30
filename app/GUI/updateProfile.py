import json
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import requests


class UpdateProfileFrame(ttk.Frame):
    def __init__(self, container):
        self.username = "Denisa"
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.Title = tk.Label(self, text="My Profile", font=("Microsoft JhengHei UI",22,"bold"))
        self.Title.grid(row=0, column=1, columnspan=2,pady=(10, 65))

        self.user_image = ImageTk.PhotoImage(Image.open("Assets/.png").resize((140, 140)))
        self.panel = tk.Label(self, image=self.user_image)
        self.panel.grid(row=1, column=2,pady=(10, 15))

        self.profile_name = ttk.Label(self, text="Username", style="BW.TLabel")
        self.profile_name.grid(row=2, column=1)

        self.wake_up_hour = ttk.Label(self, text="Wake-up Hour", style="BW.TLabel")
        self.wake_up_hour.grid(row=3, column=1)

        self.sleep_hour = ttk.Label(self, text="Sleep Hour", style="BW.TLabel")
        self.sleep_hour.grid(row=4, column=1)

        self.timer = ttk.Label(self, text="Timer", style="BW.TLabel")
        self.timer.grid(row=5, column=1)

        # values of fields
        self.profile_name_value = tk.StringVar()
        self.wake_up_hour_value = tk.StringVar()
        self.sleep_hour_value = tk.StringVar()
        self.timer_value = tk.DoubleVar()
        self.same_as_outside_lights_value = tk.BooleanVar()

        res = self.get_user('Denisa')

        self.profile_name_value.set(res['user_profile']['profile_name'])
        self.wake_up_hour_value.set(res['user_profile']['wake_up_hour'])
        self.sleep_hour_value.set(res['user_profile']['sleep_hour'])
        self.timer_value.set(res['user_profile']['timer'])
        self.same_as_outside_lights_value.set(res['user_profile']['same_as_outside_lights'])

        # boxes
        self.profile_name_box = tk.Entry(self, textvariable=self.profile_name_value, justify="center", width=25)
        self.wake_up_hour_box = tk.Entry(self, textvariable=self.wake_up_hour_value, justify="center", width=25)
        self.sleep_hour_box = tk.Entry(self, textvariable=self.sleep_hour_value, justify="center", width=25)
        self.timer_box = tk.Entry(self, textvariable=self.timer_value, justify="center", width=25)


        self.profile_name_box.grid(row=2, column=2, pady=(7, 7), ipady=7, ipadx=12)
        self.wake_up_hour_box.grid(row=3, column=2, pady=(7,7), ipady=7, ipadx=12)
        self.sleep_hour_box.grid(row=4, column=2, pady=(7,7), ipady=7, ipadx=12)
        self.timer_box.grid(row=5, column=2, pady=(7,7), ipady=7, ipadx=12)


        self.check_box = tk.Checkbutton( self, text="Same as outside lights",
                                         variable=self.same_as_outside_lights_value,
                                         onvalue=1, offvalue=0,
                                        font="Cambria")
        self.check_box.grid(row=6, column=1)

        self.B = tk.Button(self, text="Update Profile", bg='#28a745',activebackground="#25873c",fg="white",activeforeground="white",
                           font=('Microsoft JhengHei UI', 13, 'bold'), width=19, relief="flat", command = self.handleUpdate)
        self.B.grid(row=7, column=2, pady=(30,0))

        self.DeleteButton = tk.Button(self, text="Delete Profile", bg='red', activebackground="#25873c", fg="white",
                           activeforeground="white",
                           font=('Microsoft JhengHei UI', 13, 'bold'), width=19, relief="flat",
                           command=self.delete_user)
        self.DeleteButton.grid(row=8, column=2, pady=(30, 0))

        style_object = ttk.Style()
        style_object.configure("BW.TLabel", font=('Cambria', 12))

    def handleUpdate(self):
        data_set = {"profile_name": self.profile_name_box.get(),
                    "wake_up_hour": self.wake_up_hour_box.get(),
                    "sleep_hour" : self.sleep_hour_box.get(),
                    "timer": self.timer_box.get(),
                    "same_as_outside_lights":self.same_as_outside_lights_value.get()
                    }


        json_data = json.dumps(data_set)
        #print(json_data, type(json_data))
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.put(url = 'http://127.0.0.1:5000/user_profile/' + str(self.profile_name_box.get()),
                                 json = data_set,
                                 headers=headers
                                 )
        #print(response,response.json())

    def get_user(self,username):
        response = requests.get(url='http://127.0.0.1:5000/user_profile/' + str(username))
        return response.json()

    def delete_user(self):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.delete(url='http://127.0.0.1:5000/user_profile/' + str(self.username),
                                json={},
                                headers=headers
                                )












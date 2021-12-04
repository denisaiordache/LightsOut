import tkinter
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("500x500")
Label(root, text="Create User Profile", font="times 20 bold").grid(row=0, column=3)

user_image = ImageTk.PhotoImage(Image.open("userIcon.png").resize((80, 80)))
panel = Label(root, image=user_image)
panel.grid(row=1, column=3)

wake_up_hour = Label(root, text="Wake-up Hour", style = "BW.TLabel")
wake_up_hour.grid(row=2, column=2)

sleep_hour = Label(root, text="Sleep Hour", style = "BW.TLabel")
sleep_hour.grid(row=3, column=2)

timer = Label(root, text="Timer", style = "BW.TLabel")
timer.grid(row=4, column=2)

lights_color = Label(root, text="Lights color", style = "BW.TLabel")
lights_color.grid(row=5, column=2)

lights_intensity = Label(root, text="Lights intensity", style = "BW.TLabel")
lights_intensity.grid(row=6, column=2)

# values of fields
wake_up_hour_value = StringVar
sleep_hour_value = StringVar
timer_value = DoubleVar
lights_color_value = StringVar
lights_intensity_value = IntVar
same_as_outside_lights_value = BooleanVar()

# boxes
wake_up_hour_box = Entry(root, textvariable=wake_up_hour_value)
sleep_hour_box = Entry(root, textvariable=sleep_hour_value)
timer_box = Entry(root, textvariable=timer_value)
lights_color_box = Entry(root, textvariable=lights_color_value)
lights_intensity_box = Entry(root, textvariable=lights_intensity_value)

wake_up_hour_box.grid(row=2, column=3)
sleep_hour_box.grid(row=3, column=3)
timer_box.grid(row=4, column=3)
lights_color_box.grid(row=5, column=3)
lights_intensity_box.grid(row=6, column=3)

check_box = tkinter.Checkbutton(text="Same as outside lights", variable=same_as_outside_lights_value, font = "Cambria")
check_box.grid(row=7, column=2)


B = tkinter.Button(text="Submit", bg = 'light blue', font=('Times New Roman', 15, 'bold'), width='12')
B.grid(row=8, column=3)

style_object = Style()
style_object.configure("BW.TLabel",font=('Cambria', 12))




root.mainloop()

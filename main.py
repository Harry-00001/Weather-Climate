import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image , ImageTk
import requests
from dotenv import load_dotenv
import os
	

win = tk.Tk()

def result () :
	try :
		city = state.get()
			
		load_dotenv("api_key.env")
		
		api_key = os.getenv("API_KEY")
		
		data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
		
		weather_climate.config(text = f"Weather Climate :        {data.get('weather')[0].get('main')}")
		weather_description.config(text = f"Weather Description :        {data.get('weather')[0].get('description')}")
		temp.config(text = f"Temp :        {data.get('main').get('temp')}")
		pressure.config(text = f"Pressure :        {data.get('main').get('pressure')}")
		humidity.config(text = f"Humidity :        {data.get('main').get('humidity')}")
		
	except Exception as e:
		messagebox.showinfo("Error", "Try Again !")	
		
win.title("Weather")
win.geometry("600x400")
icon = tk.PhotoImage(file = "weather.png")
win.iconphoto(True , icon)



img = Image.open("weather_bg.jpg")
img = img.resize((600 , 400))

bg = ImageTk.PhotoImage(img)

background = ttk.Label(win , image = bg)
background.place(x= 0 , y=0)

state = tk.StringVar()

state_list = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
    "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
    "Uttarakhand", "West Bengal"
]

heading = ttk.Label(win , text = "Weather" , font = ("Segoe UI" , 30 , "bold") , background = "#5DADE2"  , foreground = "white")
heading.pack(pady = 10)

state_name = ttk.Combobox(win , values = state_list , textvariable = state)
state_name.pack(padx = 50 , pady = 5 , ipadx = 50)

check_button = ttk.Button (win , text = "Done" , command = result)
check_button.pack(  pady = 5)
# ~ weather climate , weather description , temp , pressure , Humidity
frame = ttk.Frame(win)
frame.pack()

weather_climate  = ttk.Label(frame, text = "Weather Climate :                   " , font = ("Arial" , 15 , "bold"))
weather_climate.pack(padx = 5 , pady = 5 , anchor = "w")

weather_description = ttk.Label(frame , text = "Weather  description :                  " , font = ("Arial" , 15 , "bold"))
weather_description.pack(pady = 5 , anchor = "w")

temp = ttk.Label(frame, text = "Temp :                   " , font = ("Arial" , 15 , "bold"))
temp.pack( pady = 5, anchor = "w" )

pressure = ttk.Label(frame, text = "Pressure  :                   " , font = ("Arial" , 15 , "bold"))
pressure.pack(pady = 5 , anchor = "w")


humidity = ttk.Label(frame , text = "Humidity  :                   " , font = ("Arial" , 15 , "bold"))
humidity.pack(pady = 5 , anchor = "w")

win.bind("<Return> " , lambda e : check_button.invoke())

win.mainloop()

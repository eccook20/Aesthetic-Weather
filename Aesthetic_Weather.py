import json, requests
from tkinter import *
from tkinter import ttk

# NWS API
# Code in this section pulls data from the NWS API

# Access Natioal Weather Service API
# Loads NWS site that corresponds to a lattitude + longitude
# This page contains a link to a JSON with forecast data
# Use getForecast() to open the forecast page
def getPoint(lat, long):
	url = "https://api.weather.gov/points/" + lat + "," + long
	response = urllib.request.urlopen(url)
	pointJSON = json.loads(response.read())	
	return getForecast(pointJSON['properties']['forecast'])

# Access NWS forecast data
def getForecast(url):
	response = urllib.request.urlopen(url)
	forecastJSON = json.loads(response.read())
	return forecastJSON

# DISPLAY
# Code in this section uses tkinter to build a GUI display

# Initializes a togglable fullscreen GUI display
def initGUI():
	# setup the window
	root = Tk()
	root.state('zoomed') # maximizes window
	root.overrideredirect(True) # removes title bar
	frame = ttk.Frame(root)
	frame.grid()
	# TODO set up fullscreen toggles
	#root.bind('<Escape>', lambda event: root.state('normal'))
	#root.bind('<F11>', lambda event: root.state('zoomed'))
	# adds a message and exit button
	ttk.Label(frame, text="Future home of Aesthetic Weather!").grid(column=0, row=0)
	ttk.Button(frame, text="Exit", command=root.destroy).grid(column=1, row=0)
	# initiate the main loop
	root.mainloop()

# RUN THE PROGRAM
# Code to start the program, calling functions defined above as needed

initGUI()
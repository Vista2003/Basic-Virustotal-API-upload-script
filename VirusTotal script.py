import requests
import sys
import tkinter as tk
from tkinter import filedialog   # Importing requested libaries
import re
import webbrowser
import time
print("Welcome to this file scanner, powered by the VirusTotal API!")
print("To proceed with the program, you must accept the EULA in the README.txt file of the folder of this file") 
input("Press your enter key if you accept or close the program if you don't accept the terms set in the EULA... ") # User starts program
print("==========================================")
input("An open file dialog box will open, please select your file! Press enter to contiune... ")
params = {'apikey': ''} # Enter your API key here
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename() # Opens file explorer
print("Uploading ", file_path, "for scanning!")
files = {'file': (file_path, open(file_path, 'rb'))}

response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
json_response = response.json()
time.sleep(1)
print(json_response["permalink"])
link = json_response["permalink"]   #Opens web browser
print("Opening your Web Browser...")
time.sleep(1)
webbrowser.open(link)
print("\n")
print("\n")
input("Press enter to exit... ")
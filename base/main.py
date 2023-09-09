# Modules
import psutil
import time
import os

# Makes Console Look Cleaner.
os.system("cls")

def check_javaw_running():
    while True:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == 'javaw.exe':
                run_autoclicker()  # Call your autoclicker function here.
                return True
        else:
            return False
        time.sleep(1)

def run_autoclicker():
    # Your autoclicker code goes here, or whatever you make.
    # Replace the following print statement with your actual autoclicker logic.
    print("Minecraft External Base")

if check_javaw_running():
    print("  Java process is running. | Minecraft External Base\n==========================================================")
else:
    print("No Java Process is found. Please make sure Minecraft is running.")

input("") # remove this once you have added your autoclicker code, or whatever your adding.

import os
import pyautogui
from speak_engine import speak

def open_notepad():
    speak("Opening Notepad")
    os.system("notepad.exe")

def open_calculator():
    speak("Opening Calculator")
    os.system("calc.exe")

def open_file_explorer():
    speak("Opening File Explorer")
    os.system("explorer.exe")

def take_screenshot():
    speak("Taking screenshot")
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot saved.")

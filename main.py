import time
import pyautogui

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

time.sleep(10)

file = open(file_path, 'r')

for line in file:
    pyautogui.typewrite(line)
    pyautogui.press('enter')

import pyautogui
import threading
import keyboard

autoclicking = False  

def autoclick():
    global autoclicking
    autoclicking = True  
    while autoclicking:
        pyautogui.click()
        pyautogui.PAUSE = 0.10 
        # pyautogui.click(button='right')  #use this if u want right click instead of left

#
def start_autoclick():
    global autoclick_thread
    if not autoclicking:  
        autoclick_thread = threading.Thread(target=autoclick)
        autoclick_thread.start()

def stop_autoclick():
    global autoclicking
    autoclicking = False 

keyboard.add_hotkey('`', start_autoclick)

keyboard.add_hotkey('/', stop_autoclick)

keyboard.add_hotkey('esc', lambda: exit())


keyboard.wait('esc')

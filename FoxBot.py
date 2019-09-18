import pyautogui as gui
import pyscreeze
import time

gui.FAILSAFE = False

def menuScreen():
    try:
        menu = gui.locateCenterOnScreen('images\\menu.png', grayscale=True, confidence=.8)
        print("Found Game")
        return True
    except Exception as ab:
        return False

def clickStart():
    try:
        start = gui.locateCenterOnScreen('images\\play.png', grayscale=True, confidence=.8)
        if start:
            gui.click(start)
            time.sleep(2)
            return True
    except Exception as cd:
        print("Couldnt Start")
        return False

def clickOk():
    try:
        ok = gui.locateCenterOnScreen('images\\ok.png', grayscale=True, confidence=.8)
        if ok:
            gui.click(ok)
            time.sleep(.08)
            return True
    except Exception as ef:
        return False

def clickOkPressed():
    try:
        ok_pressed = gui.locateCenterOnScreen('images\\ok_pressed.png', grayscale=True, confidence=.9)
        if ok_pressed:
            gui.click(ok_pressed)
            time.sleep(.08)
            return True
    except Exception as ef:
        return False

def clickLeave():
    try:
        leave = gui.locateCenterOnScreen('images\\leave.png', grayscale=True, confidence=.8)
        if leave:
            gui.click(leave)
        return True
    except Exception as gh:
        return False

def wait():
    try:
        sleep = gui.locateOnScreen('images\\sleep.png')
        if done:
            gui.click(sleep)
        return True
    except Exception as gh:
        return False

def run():
    while True:
        global state
        if menuScreen():
            state = 'not started'
        else:
            state = 'started'
        if state == 'not started':
            print("Starting FoxBot")
            clickStart()
            state = 'started'
            time.sleep(2)
        if clickOk():
            print("Found: OK")
            clickOk()
        if clickOkPressed():
            print("Found: OK Pressed")
            clickOkPressed()
        if clickLeave():
            print("Found: Leave")
            clickLeave()
            state = 'not started'
        if wait():
            print("Sleeping")
            time.sleep(.8)

run()

""" Debugging Options """
# print(clickOk())
# print(clickOkPressed())
# print(clickLeave())
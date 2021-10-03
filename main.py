from ctypes.wintypes import POINT
from PIL.ImageOps import grayscale
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

referenceFolder = 'screenshots\\'
rollPic = referenceFolder + 'Roll.png'
lockPic = referenceFolder + 'Lock.png'
brawlPic = referenceFolder + 'Brawl.png'

defaultPos = (-100, -100)
rollButton, lockButton, brawlButton = defaultPos, defaultPos, defaultPos

def moveCursor(position: Point):
    win32api.SetCursorPos(position)

def leftMouseDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def leftMouseUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def click(x, y):
    moveCursor((x, y))
    leftMouseDown()
    time.sleep(0.1)
    leftMouseUp()

def clickAndReset(x, y):
    previousX, previousY = win32api.GetCursorPos()
    click(x, y)
    moveCursor((previousX, previousY))

def drag(start: Point, end: Point):
    moveCursor(start)
    leftMouseDown()
    time.sleep(0.1)
    moveCursor(end)

def reRoll():        
    global rollButton
    if (rollButton == defaultPos):
        rollButton = pyautogui.locateCenterOnScreen(rollPic, grayscale=True, confidence=0.8)
    clickAndReset(rollButton.x, rollButton.y)

def lock():
    global lockButton
    if (lockButton == defaultPos):
        lockButton = pyautogui.locateCenterOnScreen(lockPic, grayscale=True, confidence=0.8)
    clickAndReset(lockButton.x, lockButton.y)

def brawl():
    global brawlButton
    if (brawlButton == defaultPos):
        brawlButton = pyautogui.locateCenterOnScreen(brawlPic, grayscale=True, confidence=0.8)
    clickAndReset(brawlButton.x, brawlButton.y)

while keyboard.is_pressed('esc') == False:
    if keyboard.is_pressed('r'):
        reRoll()

    if keyboard.is_pressed('l'):
        lock()

    if keyboard.is_pressed('b'):
        brawl()
    
    time.sleep(0.1)
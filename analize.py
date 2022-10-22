from vision import Vision
from settings import Settings
from windowcapture import get_screenshot, get_screenshot_grab
from PIL import Image
import cv2 as cv
import pytesseract
import os
import pyautogui
import time

config = Settings()

def needle_position(img_needle):
    """
    Anlizes screen and returns img_needle position
    """
    login_vision = Vision(img_needle)
    screen = get_screenshot(config.monitor)
    points = login_vision.find(screen, debug_mode=True)
    if points:
        x,y,w,h = points
        x = x+(w/2)
        y = y+(h/2)
        points = (x,y)
        return points

def needle_position_once(img_needle):
    """
    Anlizes screen once and returns img_needle position if found
    """
    login_vision = Vision(img_needle)
    screen = get_screenshot(config.monitor)
    points = login_vision.find(screen, debug_mode=True)
    if points:
        x,y,w,h = points
        x = x+(w/2)
        y = y+(h/2)
        points = (x,y)
        return points
    else:
        return None

def click_point(x,y):
    x = int(x)
    y = int(y)
    pyautogui.moveTo(x,y)
    time.sleep(0.5)
    pyautogui.click(x,y,button='left')
    print(f"Klikam na {x} - {y}")
    time.sleep(1)

def get_needle_and_text(top,left,width,height, debug=False):
    """
    Get's needle position and screenshots then returns text
    readed from it
    """
    img_needle_position = {"top":top, "left":left,
    "width":width, "height":height}
    screen = get_screenshot_grab(top,left,width,height)
    cv.imshow('test',screen)
    if debug:
        print("here")
        time.sleep(5)
    text = needle_text(screen, debug=debug)
    return text

def needle_text(img_needle, debug=False):
    """
    Returns text readed from image
    """
    #convert to grayscale image
    gray=cv.cvtColor(img_needle, cv.COLOR_BGR2GRAY)
    if config.state == 'debug':
        cv.imshow('test',gray)
    #memory usage with image i.e. adding image to memory
    filename = "temp/{}.jpg".format('temporary')
    cv.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    if debug:
        print(f"Text from image - {text}")
    return text
import time
import pyautogui

from .wait import until, untilClick

def back(region = 'jp'):
  untilClick('global-back', region)

def backToHome(region = 'jp'):
  untilClick('minimenu', region)
  time.sleep(0.1)
  untilClick('minimenu-home', region)
  time.sleep(0.1)
  until('home-achivement', region)
  time.sleep(0.1)

def locate(name, region = 'jp', confidence=0.9):
  return pyautogui.locateOnScreen('assets/' + region + '/' + name + '.png', confidence)

def clickHomeMenu(name, region = 'jp'):
  menuLocation = pyautogui.locateOnScreen('assets/' + region + '/home-' + name + '-inactive.png')
  pyautogui.click(menuLocation)

  time.sleep(0.4)

  # if menu is hover active, then need to click again
  if pyautogui.locateOnScreen('assets/' + region + '/home-' + name + '-active.png') is not None:
    pyautogui.click(menuLocation)

import time
import pyautogui

def until(fileName, region = 'jp', confidence=0.9):
  while True:
    itemLocation = pyautogui.locateOnScreen('assets/' + region + '/' + fileName + '.png', confidence)
    if itemLocation is not None:
      return itemLocation
      break

    time.sleep(0.3)

def untilClick(fileName, region = 'jp', confidence=0.9):
  while True:
    itemLocation = pyautogui.locateOnScreen('assets/' + region + '/' + fileName + '.png', confidence)

    if itemLocation is not None:
      pyautogui.click(itemLocation)
      return itemLocation
      break

    time.sleep(0.3)

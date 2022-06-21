import pyautogui
import time

import tools.commons as commons
import tools.wait as wait
import tools.logger as logger

def execute(region):
  logger.info('navigating to dress menu')
  commons.clickHomeMenu('dress', region)

  logger.info('going into enhance panel')
  wait.untilClick('dress-menu-enhance', region)

  logger.info('looking for available enhance button')
  wait.untilClick('enhance-button', region)

  logger.info('picking 5 medium yarn')
  mediumYarnLocation = wait.until('enhance-medium-yarn', region)
  for i in range(5):
    pyautogui.click(mediumYarnLocation)
    time.sleep(0.2)

  for i in range(2):
    wait.untilClick('global-ok-button-enabled', region)

  logger.info('waiting enhance to be completed')
  time.sleep(2)
  wait.until('global-ok-button-disabled', region, confidence=0.93)
  wait.untilClick('global-close')

  logger.done('enhance quest done! going back home')
  commons.backToHome(region)

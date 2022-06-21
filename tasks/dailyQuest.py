import time
import pyautogui

import tools.commons as commons
import tools.wait as wait
import tools.logger as logger

def execute(region = 'jp'):
  logger.info('navigating to quest menu')
  commons.clickHomeMenu('quest', region)

  logger.info('going into daily limited quest')
  wait.untilClick('quest-menu-daily', region)

  logger.info('looking into any battle')
  wait.untilClick('daily-quest-battle', region)

  logger.info('opening auto-battle dialog')
  wait.untilClick('daily-quest-auto', region)

  incrementButtonLocation = wait.until('daily-quest-increment', region)
  for i in range(4):
    pyautogui.click(incrementButtonLocation)
    time.sleep(0.15)

  for i in range(3):
    wait.untilClick('global-ok-button-enabled', region)
    time.sleep(1)

  logger.done('daily quest completed! going back to home')
  commons.backToHome(region)
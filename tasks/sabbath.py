import time
import pyautogui

import tools.commons as commons
import tools.wait as wait
import tools.logger as logger

def execute(region = 'jp'):
  logger.info('navigating to sabbath menu')
  commons.clickHomeMenu('sabbath', region)

  logger.info('picking some battle')
  wait.untilClick('sabbath-menu-entry', region)
  wait.until('sabbath-header', region)
  wait.untilClick('sabbath-battle-button', region)

  logger.info('starting battle')
  wait.untilClick('sabbath-battle-start', region)

  logger.info('waiting to enable autoplay')
  wait.untilClick('sabbath-autoplay-button', region)

  logger.info('autoplay enabled...waiting for results')
  while True:
    if commons.locate('sabbath-user-icon', region) is not None:
      logger.warn('battle finished')
      userIconLocation = commons.locate('sabbath-user-icon', region)
      while commons.locate('sabbath-back-to-top-button', region) is None:
        pyautogui.click(userIconLocation)
        time.sleep(0.2)
      wait.untilClick('sabbath-back-to-top-button', region)
      break
    else:
      time.sleep(5)

  logger.done('sabbath battle completed! going back to home')
  commons.backToHome(region)

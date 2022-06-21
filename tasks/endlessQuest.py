import pyautogui

import tools.commons as commons
import tools.wait as wait
import tools.logger as logger

def execute(region = 'jp'):
  logger.info('navigating to quest menu')
  commons.clickHomeMenu('quest', region)

  # optional quest 1
  # endless quest

  # wait until menu available then click
  logger.info('entering enless quest')
  wait.untilClick('quest-menu-endless', region)

  # do endless quest until you can't
  logger.info('entering endless quest')
  wait.until('endless-header', region)
  while commons.locate('endless-entry-disabled', region) is None:
    logger.info('endless quest available! starting battle...')
    # do endless quest
    wait.untilClick('endless-entry-enabled', region)
    wait.untilClick('endless-battle-start', region)
    logger.info('battle started, waiting to finish')
    # when quest is finished click until
    userIconLocation = wait.until('global-battle-user-icon', region)
    logger.info('battle finished! finalizing...')
    while commons.locate('endless-stage-select', region) is None:
      pyautogui.click(userIconLocation)
      time.sleep(0.2)
    logger.info('stage select button shown! clicking...')
    wait.untilClick('endless-stage-select', region)
    logger.info('waiting for menu...')
    wait.until('endless-header', region)
  logger.done('endless quest complete! back to home')

  commons.backToHome(region)

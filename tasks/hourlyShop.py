import tools.commons as commons
import tools.wait as wait
import tools.logger as logger

def execute(region = 'jp'):
  logger.info('navigating to shop menu')
  commons.clickHomeMenu('shop', region)

  logger.info('entering hourly shop')
  wait.untilClick('shop-menu-hourly', region)
  wait.untilClick('global-close', region)
  commons.backToHome(region)

import time
import pyautogui

import tools.commons as commons
import tools.wait as wait
import tools.logger as logger

import tasks.dailyQuest as dailyQuest
import tasks.endlessQuest as endlessQuest
import tasks.hourlyShop as hourlyShop
import tasks.dressEnhance as dressEnhance
import tasks.sabbath as sabbath

# jp | en
region = 'en'

#
# section 1: endless quest
#
endlessQuest.execute(region)

#
# section 2: visit hourly shop
#
hourlyShop.execute(region)

#
# section 3: dress upgrade
#
dressEnhance.execute(region)

#
# section 4: daily quest exercise
#
dailyQuest.execute(region)

#
# section 5: sabbath battle
#
sabbath.execute(region)

#
# section 6: collecting daily achivement
#
logger.done('daily achivements completed! collecting rewards')
wait.untilClick('home-achivement', region)
wait.untilClick('achivement-daily', region)
wait.untilClick('achivement-collect-button', region)
wait.untilClick('global-ok-button-enabled', region)
time.wait(1)
wait.untilClick('global-close', region)
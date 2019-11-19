import random
import calendar
import datetime
def getRandomReward():
	now = datetime.datetime.now()
	current_month_range = calendar.monthrange(now.year, now.month)[1]
	random_reward = random.randint(5, 10)
	random_day = random.randint(1, current_month_range)
	print("The random day to give reward is %d" %(random_day))
	print("The random reward amount is %d" %(random_reward))
getRandomReward()

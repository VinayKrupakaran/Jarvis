#!/usr/bin/env python

import datetime

User_Name = 'Vinay'

def welcome_func():
#This function provides a welcome interface to the user
	time = datetime.datetime.time(datetime.datetime.now()).isoformat()
	print '%s %s' %(current_time_of_day(time), User_Name)


def current_time_of_day(time):
	time = int(time[:2])
	if time >= 6 and time < 12:
		return 'Good Morning'
	elif time >= 12 and time <= 18:
		return 'Good Afternoon'
	elif time > 18 and time < 22:
		return 'Good Evening'
	else:
		return 'You\'re up late tonight'

welcome_func()

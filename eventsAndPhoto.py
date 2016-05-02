#!/usr/bin/env python
#Author: Mike R
#Date: 5/2/2016
#gets astrophotography targets for current month

import datetime
import webbrowser

#Another option could also ask user for the targets for a specific month as well.

now=datetime.datetime.now()

#get current month
monthNum=now.month

#if X, then
#go to website for the appropriate data
if monthNum==1:
	webbrowser.open("http://www.neurohack.com/Astrophotography/JanuaryTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#january")

if monthNum==2:
	webbrowser.open("http://www.neurohack.com/Astrophotography/FebruaryTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#february")

if monthNum==3:
	webbrowser.open("http://www.neurohack.com/Astrophotography/MarchTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#march")

if monthNum==4:
	webbrowser.open("http://www.neurohack.com/Astrophotography/AprilTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#april")
	
if monthNum==5:
	webbrowser.open("http://www.neurohack.com/Astrophotography/MayTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#may")

if monthNum==6:
	webbrowser.open("http://www.neurohack.com/Astrophotography/JuneTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#june")
	
if monthNum==7:
	webbrowser.open("http://www.neurohack.com/Astrophotography/JulyTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#july")

if monthNum==8:
	webbrowser.open("http://www.neurohack.com/Astrophotography/AugustTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#august")

if monthNum==9:
	webbrowser.open("http://www.neurohack.com/Astrophotography/SeptemberTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#september")

if monthNum==10:
	webbrowser.open("http://www.neurohack.com/Astrophotography/OctoberTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#october")

if monthNum==11:
	webbrowser.open("http://www.neurohack.com/Astrophotography/NovemberTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#november")

if monthNum==12:
	webbrowser.open("http://www.neurohack.com/Astrophotography/DecemberTargets.html")
	webbrowser.open("http://www.amsky.com/calendar/events/#december")

#Other options would be to read from the site and provide data in a nice table

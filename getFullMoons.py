#!/usr/bin/env python
#Author: Mike R
#Will require install of PyEphem: pip install ephem
#Gets list of full and new moons for the year

import ephem

d1 = ephem.next_full_moon('2016')

month=1
while month<13:
    
    print "------------------------------"
    if month==1:
        print "January"
    elif month==2:
        print "February"
    elif month==3:
        print "March"
    elif month==4:
        print "April"
    elif month==5:
        print "May"
    elif month==6:
        print "June"
    elif month==7:
        print "July"
    elif month==8:
        print "August"
    elif month==9:
        print "September"
    elif month==10:
        print "October"
    elif month==11:
        print "November"
    elif month==12:
        print "December"
    print "------------------------------"
    #New Moon
    d2 = ephem.next_new_moon('2016/' + str(month))
    print "New Moon: " + str(d2)

    #Full Moon
    d3 = ephem.next_full_moon('2016/' + str(month))
    print "Full Moon: " + str(d3)
    print "------------------------------\n"
    month=month+1

#!/usr/env/python
#Author: Mike R
#Get Longitude and Latitude of any place using Google Maps API

from bs4 import BeautifulSoup
import urllib

html=urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/xml?address=Crater+Lake,+OR&key=[Google API Key Here]")

bt=BeautifulSoup(html.read(), "lxml") #read, parser wanted. By default uses HTML which is not the best available.

for latitude in bt.find('lat'):
    print "Latitude: " + latitude

for longitude in bt.find('lng'):
    print "Longitude: " + longitude

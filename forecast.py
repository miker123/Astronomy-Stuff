#!/usr/bin/env python
#Author: Mike R
#Provides average cloud coverage and weather forecasting for free

import forecastio
import datetime
api_key = "" #API KEY Here. FRee and can register at their site.
lat = -31.967819
lng = 115.87718

#Gets temperature based upon GMT
forecast = forecastio.load_forecast(api_key, lat, lng)

#minute for next hour
#hourly only for next 2 days.
#daily for 2 weeks

#This is in GMT. Not sure how to get it to local time.

#more details at https://developer.forecast.io/docs/v2
byHour = forecast.hourly()
print byHour.summary
print byHour.icon
for hourlyData in byHour.data:
    print "Date: "+ str(hourlyData.time)
    print "Temperature: " + str(hourly.temperature)
    print "Cloud Cover: " + str(hourlyData.cloudCover)

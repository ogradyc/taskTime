#!/usr/bin/python -tt
# Copyright 2012 Cameron O'Grady.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Part of a project to apply my Python curiosity to improve everyday tasks
# taskTime is the application that will eventually control my life (if I want it to)
# http://c9n.org

import sys
import time
import datetime


def waitTime(xMin):
# Create Module that figures out how long the program needs to wait
  ''' Called by taskTime
  Input: - Minute interval x (example 6 minute interval)
  Output - Amount of minutes it will be till the next x interval 
  
  xMin = minute interval
  yRem = remainder till next closest minute interval
  zTime = current time
  
  def WaitTime(xMin)
    zTime = current.dateTime
    yRem = datetime.minutes %xMin
    result = createNewTimeFrom (zTime.hour, yRem, zTime.second, zTime.milisecond) 
    return result
  '''
  t = datetime.datetime.utcnow()
  print 'waitTime - Step 1'
  print xMin
  print t
  print t.minute
  print 't.minute % xMin'
  yRem = t.minute%xMin
  print xMin - yRem
  zResult = xMin - t.minute%xMin + t.minute
  print zResult
  print 'waitTime - Step 2 - Need to create a something of how much time to wait'

  print 'waitTime - Step 3 - does this wait?'
  future = datetime.datetime(t.year, t.month, t.day, t.hour, zResult, 00, 00)
  print future
  #future = datetime.datetime(now.year,now.month,now.day,now.hour,now.min)
  #time.sleep((future-t).seconds)
  print 'time is now, ask question'
  return zResult
  
  # if for some reason this script is still running
  # after a year, we'll stop after 365 days
  #for i in xrange(0,365):
      # sleep until 2AM
      #t = datetime.datetime.today()
      #print 'waitTime - Step 4 - inside a for loop'
      #future = datetime.datetime(t.year,t.month,t.day+(t.hour >= 2 ),2,0)
      #time.sleep((future-t).seconds)

      # do 2AM stuff
  

  
  
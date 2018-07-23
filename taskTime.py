#!/usr/bin/python -tt
# Copyright 2012 Cameron O'Grady.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Using Python curiosity to improve everyday tasks
# http://c9n.org/tasktime ** create this webpage

import sys          # I think this has read and write and whatnot 
import time         # important for sleep time
import datetime     # Date and Time Module
import re           # Regular expressions
#import msvcrt       # Not sure what this does. 
import gspread      # Google Sheets
from oauth2client.service_account import ServiceAccountCredentials

interval = 2


def logOnToGoogle():
  #https://github.com/burnash/gspread/issues/138
  #https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
   

  # use creds to create a client to interact with the Google Drive API
  scope = [
      'https://spreadsheets.google.com/feeds',
      'https://www.googleapis.com/auth/drive'
  ]
  creds = ServiceAccountCredentials.from_json_keyfile_name('taskTimeGraphData-8913f891ca5d.json', scope)
  client = gspread.authorize(creds)
   
  # Find a workbook by name and open the first sheet
  # Make sure you use the right name here.
  sheet = client.open("timeSheet").sheet1
   
  # Extract and print all of the values
  list_of_hashes = sheet.get_all_records()
  #print(list_of_hashes)
  return sheet


def waitTime(xinterval):
 # Module that figures out how long the program needs to wait
  t = datetime.datetime.utcnow()
  secSyncTime = datetime.datetime(t.year, t.month, t.day, t.hour, t.minute, 00, t.microsecond)
  yRem = t.minute%xinterval
  zMin = xinterval - yRem
  result = secSyncTime + datetime.timedelta(minutes = zMin)
  return result


def readFile():
 # Module that reads the file and stores the last 3 lines as variables
 # Going to start with just the last line as a variable for simplicity
  lastLine = 'nothingRecorded'
  result = lastLine
  return result


def writeRow(input):
  # Module that writes to a google sheet spreadsheet
  sheet = logOnToGoogle()
  row = input
  index = 2
  sheet.insert_row(row, index)


def writeFile(input):
  # Module that writes to a file, then closes it
  with open("taskTime.txt", "a") as f:
    f.write(input)
    f.close()


def writeHeader():
# Module that writes the header with a timestamp and a local time stamp 
  utcTime = datetime.datetime.utcnow()
  localTime = datetime.datetime.now()
  prev_hour_min = utcTime.strftime('%H:%M')  
  date_header = utcTime.strftime('Header - UTC %m/%d/%Y @ %H:%M - %I:%M%p') + ' - ' + 'Interval ' + str(interval) + 'min - ' + localTime.strftime('%A - Local Time %m/%d/%Y @ %I:%M%p')
  header = date_header + '\n'
  writeFile(header)


def writeRecord(future):
# Module that writes the record with a UTC timestamp
  utcTime = datetime.datetime.utcnow()
  localTime = datetime.datetime.now()
  intervalMilliseconds = interval * 60000
  local_hour_min = localTime.strftime('%H:%M')
  hour_min = future.strftime('%H:%M')
  prev_hour_min = (utcTime - datetime.timedelta(minutes = interval)).strftime('%H:%M')
  record = ('  ' + '\t' + utcTime.strftime('%m/%d/%Y @ ') + prev_hour_min + '-' + hour_min + '\t' + readFile() + '\n')
  googRecord = ["", utcTime.strftime('%Y-%m-%d'), "TestEngineer", readFile(), intervalMilliseconds, interval, local_hour_min. prev_hour_min, hour_min]
  prev_hour_min = hour_min
  writeFile(record)
  writeRow(googRecord)


def writeLastLine():
# Module that replaces the last line with "nothing" to encourage input again.
# copies either the last line or the 2nd to last line depending on if its populated with something other than "nothing"
  result = 0
  return result


def taskTime():
# Module that triggers the loop to fire every interval
# Depends on time, and datetime
# Calls writeHeader, waitTime, writeRecord
  run = True
  x = 0
  y = 0
  writeHeader()
  while run == True:
    t = datetime.datetime.utcnow()
    print('Loop has run for ' + str(x) + ' cycles or ' + str(y) + ' minutes')
    x = x +1
    y = y + interval

    future = waitTime(interval)
    print('current time')
    print(t)
    print('future time')
    print(future)
    time.sleep((future-t).seconds)
    print('Done with sleeping')
    writeRecord(future)

    print('Checking for Zeros')
    utcTime = datetime.datetime.utcnow()
    if utcTime.minute == 00:
      writeHeader()


# Define a main() function that calls tasktime.
def main():  
  print('Main Calling taskTime')
  #logOnToGoogle()
  taskTime()
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
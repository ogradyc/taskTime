#!/usr/bin/python -tt
# Copyright 2012 Cameron O'Grady.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Using Python curiosity to improve everyday tasks
# http://c9n.org/projectNumGen ** create this webpage

# Use a reg-ex to search task time and copy in all the entries - and calculate the time spend on it. 
# Add notepad interface at the bottom of everything - figure out how to not write to the end of a file.


import re           # Regular expressions
import datetime     # Date and Time Module

def projectNumGen(projectTemplate, prefix):
# Open and read the TemplateFile.
  projectNotes = open(projectTemplate, 'rU')
  projectNotes_text = projectNotes.read()
  # Could process the file line-by-line, but regex on the whole text at once is even easier.

  
  projectNumber = (projectNumberGenerator())
  prefixProjectNumber = prefix + projectNumber
  revisedOMNotes_text = ( re.sub('projectNumber',prefixProjectNumber,projectNotes_text)  )
  
  timeStamp = (currentTime())
  revisedOMNotes_text = ( re.sub('currentTime',timeStamp,revisedOMNotes_text)  )
  
  
  writeFile(revisedOMNotes_text, prefixProjectNumber)
  projectNotes.close()
  
  # Place where I found how to replace words in a file
  # http://www.daniweb.com/software-development/python/threads/70426/replace-words-in-a-file#


def currentTime():
 # Module that provides a timestamp for noteGen Creation
  utcTime = datetime.datetime.utcnow()
  localTime = datetime.datetime.now()
  result = utcTime.strftime('UTC %Y-%m-%d @ %H:%M:%S - %I:%M:%S%p') + ' - ' + localTime.strftime('%A Local Time %m/%d/%Y @ %I:%M:%S%p  %f mili')
  return result


def projectNumberGenerator():
 # Module that provides a project number based off of the current time
  utcTime = datetime.datetime.utcnow()
  localTime = datetime.datetime.now()
  result = utcTime.strftime('%Y%m%d%H%M%S')
  # if you ever want Miliseconds added use: result = utcTime.strftime('%Y%m%d%H%M%S%f')
  return result


def writeFile(input, projectNumber):
  # Module that writes to a file, then closes it
  fileName = projectNumber + ' - Notes.txt'
  with open(fileName, "a") as f:
    f.write(input)
    f.close()


# Define a main() function that calls projectNumGen.
def main():  
  projectNumGen('blankProject.txt', 'Proj ')
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
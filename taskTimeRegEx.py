#!/usr/bin/python -tt
# Copyright 2012 Cameron O'Grady.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Using Python curiosity to improve everyday tasks
# http://c9n.org/taskTimeRegEx ** create this webpage

# Use a reg-ex to search task time and copy in all the entries - and calculate the time spend on it. 
# Add notepad interface at the bottom of everything - figure out how to not write to the end of a file.


import re           # Regular expressions
import datetime     # Date and Time Module
import sys

def taskTimeRegEx(filename, taskOutputTemplate):
# Open and read the file.
  template = open(taskOutputTemplate, 'rU')
  template_text = template.read()
  
  
  notes = open(filename, 'rU')
  notes_text = notes.read()
  # Could process the file line-by-line, but regex on the whole text at once is even easier.


  projectNumber = re.compile('\A.*')
  theprojectNumber = printResult(projectNumber, notes_text)
  revisedNotes_text = ( re.sub("theprojectNumber",theprojectNumber,template_text)  )


  count = 0
  theTasks = ''
  f = open('python/taskTime/taskTime.txt', 'rU')
  for line in iter(f):
    #print line
    taskSearchProjNum = re.compile('.*20121018045430.*')
    searchResult = taskSearchProjNum.search(line)
    if searchResult:
      theTaskSearchProjNum = printResult(taskSearchProjNum, line) + '\n'
      theTasks = theTasks + theTaskSearchProjNum
      #writeFile(filename, theTaskSearchProjNum)
      count = count + 1
  #writeFile(filename, 'Count ' + str(count))
  f.close()
  timeSpentOnProject = count * 6 # going to have to get this to pull the interval from somewhere if I want to not have it break.
  revisedNotes_text = ( re.sub("theTasks",theTasks,revisedNotes_text)  )
  revisedNotes_text = ( re.sub("theCount",str(count),revisedNotes_text)  )
  revisedNotes_text = ( re.sub("theTimeSpentOnProject",str(timeSpentOnProject),revisedNotes_text)  )


  timeStamp = (currentTime())
  revisedNotes_text = ( re.sub('currentTime',timeStamp,revisedNotes_text)  )
  
  
  createProjectNumber = (projectNumberGenerator())
  revisedNotes_text = ( re.sub('createProjectNumber',createProjectNumber,revisedNotes_text)  )
  
  
  writeFile(filename, revisedNotes_text)
  notes.close()
  
  # Place where I found how to replace words in a file
  # http://www.daniweb.com/software-development/python/threads/70426/replace-words-in-a-file#
  
  
def currentTime():
 # Module that provides a timestamp for noteGen Creation
  utcTime = datetime.datetime.utcnow()
  localTime = datetime.datetime.now()
  result = utcTime.strftime('UTC %Y-%m-%d @ %H:%M:%S - %I:%M:%S%p') + ' - ' + localTime.strftime('%A Local Time %m/%d/%Y @ %I:%M:%S%p')
  return result

  
def projectNumberGenerator():
 # Module that provides a project number based off of the current time
  utcTime = datetime.datetime.utcnow()
  localTime = datetime.datetime.now()
  result = utcTime.strftime('%Y%m%d%H%M%S')
  # if you ever want Miliseconds added use: result = utcTime.strftime('P %Y%m%j%H%M%S%f')
  return result
  

def printResult(var, text):
  # Module that helps me print my results
  searchResult = var.search(text)
  result = searchResult.group()
  print result
  return result


# def writeFile(input, ticket):
  # Module that writes to a file, then closes it
#  ticketName = 'TC ' + ticket + ' - OM Notes.txt'
#  with open(ticketName, "a") as f:
#    f.write(input)
#    f.close()
    
    
def writeFile(filename, input):
  # Module that writes to a file, then closes it
  with open(filename, "a") as f:
    f.write(input)
    f.close()


# Define a main() function that calls taskTimeRegEx.
def main():  
  taskTimeRegEx('Proj 20121018045430 - Notes.txt', 'taskOutputTemplate.txt')
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
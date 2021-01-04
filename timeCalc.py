import time
import re
import csv

#open the file and read into a variable
#TODO: alter this so that it's reading from serial input rather than csv
with open('times.csv',encoding='ASCII') as readTimes:
    times = readTimes.read()

#read the timestamps into an array using regex
#TODO: add additional regex to exclude typos and ignore times outside of a reasonable range ex (36:85:94)
timePattern = re.compile(r'(\d{2}):(\d{2}):(\d{2})')
timearray = re.findall(timePattern,times)

#read user input, parse it with regex, and add it to an array of times
#TODO add same regex logic as in TODO above, move logic for serial input into while loop so it is read in parallel 
userTime = ""
userTimeArray = []
while(userTime != 'quit'):
    userTime = input("Please enter a time in the format hh:mm:ss or type quit to exit ")
    userTimeTemp = re.findall(timePattern,userTime)
    userTimeArray.append(userTimeTemp)
#pop statement removes the user's last input ('quit')
userTimeArray.pop()   

#calculates difference between individual elements in each parallel array
"""TODO: make this actually work for each element in each array, as right now it is only working for the final element in the array (need to have a think on this one), add logic so that if the minute or hour rolled over the calculation takes that into account as well (probably use the compiled regex to pull out individual time units first, then use a series of if statements to do the calculations separately before reassembling them) """
for i in range(0,len(userTimeArray)):
    finalTimes = []
#recasting the elements this way feels ugly but it was the best way I could think to do this 
    finalTimes.append(str(int(userTimeArray[i][0][0]) - int(timearray[i][0])) + ':' + 
                      str(int(userTimeArray[i][0][1]) - int(timearray[i][1])) + ':' +
                      str(int(userTimeArray[i][0][2]) - int(timearray[i][2])))
    
print(finalTimes)
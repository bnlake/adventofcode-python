import os
import re

# We need to parse a frequency change from str to int
def parseFreqChangeToInt(string):
    if type(string) == str:
        regex = re.compile('([-+]){1}([0-9]+)')
        match = regex.match(string)
        if (match.group(1) == '-'):
            return 0 - int(match.group(2))
        else:
            return 0 + int(match.group(2))
    elif type(string) == int:
        return 0 + string
    else:
        raise TypeError('Cannot parse invalid type')


inputFilePath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '1a-in.txt'))
file = open(inputFilePath, 'r')

runningTotal = 0

while True:
    # Read next line
    line = file.readline()
    # Exit loop if end of file reached
    if not line:
        break
    # Use our parse function to turn string into int
    runningTotal += parseFreqChangeToInt(line)


print(runningTotal)

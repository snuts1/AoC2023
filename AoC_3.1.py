import re
import numpy

f = open('C:/Users/steve/Documents/AoC 2023/d3/data.txt')
data = f.readlines()
symbolMap=[]
numberMap=[]
starMap=[]
validNumbers=[]

#ok this took a while to figure out. replaces any match in the symb pattern with
#'X' for each line in the input data. DONT PUT = AT THE END IDK WHY
symb=re.compile(r'[=@#$%&*+/-]')
test2=[symb.sub('X',x) for x in data]

#get coords of all symbols
for line in test2:
    symbolIter=re.finditer(r'X',line)
    for s in symbolIter:
        symbolMap.append((test2.index(line),s.span()[0]))

#get coords of all numbers
for line in data:
    numberIter=re.finditer(r'\d+',line)
    for n in numberIter:
        numberMap.append([data.index(line),n.span()[0],n.span()[1]-n.span()[0]])

#checks distance between 2 points and returns whether they are adjacent
def dCheck(p1,p2):
    dX=abs(p1[0]-p2[0])
    dY=abs(p1[1]-p2[1])
    d=((dX**2)+dY**2)**(0.5)
    return d < 2

#takes a number coord (x,y,#digits) and checks all digit spots against the list of symbol coords
def numberChecker(numberLoc):
    numDigits=numberLoc[2]
    valid=False
    thisNum=''
    for i in range(numDigits):
        digitCol=numberLoc[1]+i
        digitRow=numberLoc[0]
        for y in symbolMap:
            if dCheck((digitCol,digitRow),(y[1],y[0])):
                valid=True
        thisNum=thisNum + data[digitRow][digitCol]
    if valid:
        return int(thisNum)
    else:
        return 0
        
#check all numbers
output=[numberChecker(x) for x in numberMap]
print(sum(output))



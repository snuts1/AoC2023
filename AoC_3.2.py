import re
import numpy

f = open('C:/Users/steve/Documents/AoC 2023/d3/data.txt')
data = f.readlines()

numberMap=[]
starMap=[]

#checks distance between 2 points and returns whether they are adjacent
def dCheck(p1,p2):
    dX=abs(p1[0]-p2[0])
    dY=abs(p1[1]-p2[1])
    d=((dX**2)+dY**2)**(0.5)
    return d < 2

#get coords of all numbers
for line in data:
    numberIter=re.finditer(r'\d+',line)
    for n in numberIter:
        numberMap.append([data.index(line),n.span()[0],n.span()[1]-n.span()[0]])

#get coords of all stars
for line in data:
    starIter=re.finditer(r'[*]',line)
    for s in starIter:
        starMap.append((data.index(line),s.span()[0]))

#this does the thing
def gearChecker(starLoc):
    ratios=[]
    thisGearRatio=0
    adjNumberCount=0
    starCol=starLoc[1]
    starRow=starLoc[0]
    thisNum=''
    for n in numberMap:
        numDigits=n[2]
        thisNum=data[n[0]][n[1]:n[1]+n[2]]
        adj=False
        for i in range(numDigits):
            if dCheck((starCol,starRow),(n[1]+i,n[0])):
                adj=True
        if adj:
            adjNumberCount+=1
            ratios.append(thisNum)      
    if adjNumberCount ==2:
        return (int(ratios[0])*int(ratios[1]))
    else:
        return 0

output2=[gearChecker(x) for x in starMap]
print(sum(output2))
        

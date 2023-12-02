import re
import numpy

f = open('C:/Users/steve/Documents/AoC 2023/d2/data.txt')
data = f.readlines()

def numberize(bit): #numberizer to allow array use
    try:
        return int(bit)
    except:
        return 0
    
def parser(dataLine):
    #separate by : ; , space
    chopped=re.split(r':|;|,| |\n',dataLine)

    #get array of indices for color words and -1 to get the preceding number
    redWords=numpy.array([i for i,x in enumerate(chopped) if x=='red'])-1
    blueWords=numpy.array([i for i,x in enumerate(chopped) if x=='blue'])-1
    greenWords=numpy.array([i for i,x in enumerate(chopped) if x=='green'])-1



    skrewed=numpy.array(list(map(numberize,chopped))) #numberize the list to convert to array, which accepts multiple index references

    #use try in case a color is absent
    try:
        redNums=skrewed[redWords]
    except:
        redNums=[0]
    try:
        blueNums=skrewed[blueWords]
    except:
        blueNums=[0]
    try:
        greenNums=skrewed[greenWords]
    except:
        greenNums=[0]

    #only care max of each color
    bigRed=max(redNums)
    bigBlue=max(blueNums)
    bigGreen=max(greenNums)

    #output for each line [GameID, maxRed, maxBlue, maxGreen]
    return [int(chopped[1]),bigRed,bigGreen,bigBlue]

output=list(map(parser,data))
print(output)
def scoreChecker(line):
    if int(line[1])<=12 and int(line[2])<=13 and int(line[3])<=14:
        return int(line[0])
    else:
        return 0

score=list(map(scoreChecker,output))

print((score))
print(sum(score))

#part 2
def powerChecker(line):
    p1=int(line[1])
    p2=int(line[2])
    p3=int(line[3])
    return p1*p2*p3
power=list(map(powerChecker,output))
print(sum(power))    
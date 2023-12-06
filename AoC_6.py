import re
import math

f=open('C:/Users/LabAdmin/Documents/Advent2023/d6/data.txt')
data=f.readlines()

pattern=re.compile('[:\D+]')
times=[int(x) for x in pattern.split(data[0]) if x!='']
records=[int(x) for x in pattern.split(data[1]) if x!='']


def tdChart(t,r):
        ts=list(range(t))
        d=[x*(t-x) for x in ts]
        wins=[1 for x in d if x>r]
        return sum(wins)

output=[tdChart(times[i],records[i]) for i in list(range(len(times)))]
#print(output)
total=math.prod(output)
#print(total)

### PART 2

pattern2=re.compile('[:]')
time2=int([re.sub(r'[ +\n]','',x) for x in pattern2.split(data[0]) if x!=''][1])
record2=int([re.sub(r'[ +\n]','',x) for x in pattern2.split(data[1]) if x!=''][1])
#print(time2)
#print(record2)
output2=tdChart(time2,record2)
print(output2)
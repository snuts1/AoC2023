import re
import math

f=open('C:/Users/LabAdmin/Documents/Advent2023/d4/test.txt')
data=f.readlines()

#parse lines to 2 lists winners | numbers
def splitNCheck(line):
    split=re.split(r'[|]',line)
    winners=re.split(r' ',split[0])
    mine=re.split(r'[ +\n]',split[1])
    mineClean=[0 if x=='' else x for x in mine]
    return checker(winners,mineClean)

#check each number against winners
def checker(ws,ns):
    matches=0
    tally=0
    for n in ns:
        isMatch=False
        isMatch=any(x for x in ws if x==n)
        if isMatch:
            matches+=1
    if matches>0:
        tally=1
    if matches>1:
        tally=2**(matches-1)
    return tally
#output=[splitNCheck(line) for line in data]
#print(sum(output))

### part 2
#new card list [card#, winner side, my number side, # of copies, ready/done to indicate looping status]
nuCards=[re.split(r'[:|]',card)+[1]+['ready'] for card in data]
nuCards=list(enumerate(nuCards))
def checker2(card):
    #clean up spaces and nulls
    winners=re.split(r' ',card[1][1])
    mine=re.split(r'[ +\n]',card[1][2])
    mineClean=[0 if x=='' else x for x in mine]
    copies=card[1][3]
    matches=0
    global nuCards
    print(card)
    if card[1][4]=='ready':
        for n in mineClean:
            isMatch=False
            isMatch=any(x for x in winners if x==n)
            if isMatch:
                matches+=1
        nuCards=[(n,[a,b,c,int(d)+(1),e]) if (matches+card[0])>=n>card[0] else (n,[a,b,c,d,e]) for (n,[a,b,c,d,e]) in nuCards]
        nuCards=[(n,[a,b,c,d,'done']) if n==card[0]  else (n,[a,b,c,d,e]) for (n,[a,b,c,d,e]) in nuCards]
    return nuCards
#checker2(nuCards[2])
#print(output2)
#print(nuCards)
output2=[checker2(line) for line in nuCards]
output3=[x for (n,[a,b,c,x,e]) in output2[-1]]
print(output3)

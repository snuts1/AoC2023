import re
import polars

f=open('C:/Users/LabAdmin/Documents/Advent2023/d7/data.txt')
data=f.readlines()

line=data[0]
split1=line.split(r' ')
splitHand=list(split1[0])
print(split1)
print(splitHand)
faceCardDict=dict(A=14,K=13,Q=12,J=11,T=10)
#ima just go ahead and get rid of the fking letters now because i think it will cause problems later


#make a list: hand, wager, hand type?, rank
parsed=[[line.split(r' '),0,0] for line in data]
#defaced=[[re.sub(r'[\w]',dict[x[0]],x)]]
def defacer(line):
    chars=list(line[0][0])
    chars=[faceCardDict[x] if x in faceCardDict.keys() else x for x in chars]
    return chars
#better list: hand list, wager, hand type?, rank
parsed2=[[defacer(line),line[0][1],line[1],line[2]] for line in parsed]
print(parsed2)

def handChecker(hand):
    matchCount=[hand.count(x) for x in hand]
    #print(matchCount)
    if matchCount.count(5)==5:
        return 7
    elif matchCount.count(4)==4:
        return 6
    elif matchCount.count(3)==3 and matchCount.count(2)==2:
        return 5
    elif matchCount.count(3)==3 and matchCount.count(1)==2:
        return 4
    elif matchCount.count(2)==4:
        return 3
    elif matchCount.count(2)==2:
        return 2
    elif matchCount.count(1)==5:
        return 1
    else:               # there shouldn't be any 0s
        return 0
#print(handChecker([4,4,4,4,4]))

checked=[[a,b,handChecker(a),d] for [a,b,c,d] in parsed2]  
print(checked)
sortedOnce=sorted(checked, key=lambda checked: checked[2])
squaredUp=[[int(a[0]),int(a[1]),int(a[2]),int(a[3]),int(a[4]),int(b),int(c),int(d)] for [a,b,c,d] in checked]

df=polars.DataFrame({"c1": squaredUp[0][0], 
                     "c2": squaredUp[0][1], 
                     "c3": squaredUp[0][2], 
                     "c4": squaredUp[0][3], 
                     "c5": squaredUp[0][4], 
                     "bet":squaredUp[0][5],
                     "type":squaredUp[0][6]})
#print(df)
for i in range(1,len(squaredUp)-1):
    df2=polars.DataFrame({"c1": squaredUp[i][0], 
                        "c2": squaredUp[i][1], 
                        "c3": squaredUp[i][2], 
                        "c4": squaredUp[i][3], 
                        "c5": squaredUp[i][4], 
                        "bet":squaredUp[i][5],
                        "type":squaredUp[i][6]})
    df.extend(df2)

ranked=df.sort(["type","c1","c2","c3","c4","c5"],descending=False)
print(ranked)
ranked=ranked.with_row_count()
ranked=ranked.with_columns(((polars.col("row_nr")+1)*(polars.col("bet")).alias("score")))
#relist=[]
#print(sortedOnce)
#for i in range(len(ranked)):
 #   relist.append(ranked[i])
print(ranked)
print(ranked.select(polars.sum("row_nr")))
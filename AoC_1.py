f = open('C:/Users/steve/Documents/AoC 2023/inputFile.txt','r')
inputWhole = f.readlines()

#check for the first instance of a specific text number
def textChecker(inputLine,num):
    try:
        return inputLine.index(num)
    except:
        return 9999

#compare text number indices and fix the first one (forwards)
def textFixer(inputLine):
    outputLine=inputLine
    first=textChecker(inputLine,'one')
    if first < 9999:
        outputLine=inputLine.replace("one","1")
    if textChecker(inputLine,'two')<first:
        first=textChecker(inputLine,'two')
        outputLine=inputLine.replace("two","2")
    if textChecker(inputLine,'three')<first:
        first=textChecker(inputLine,'three')
        outputLine=inputLine.replace("three","3")
    if textChecker(inputLine,'four')<first:
        first=textChecker(inputLine,'four')
        outputLine=inputLine.replace("four","4")
    if textChecker(inputLine,'five')<first:
        first=textChecker(inputLine,'five')
        outputLine=inputLine.replace("five","5")
    if textChecker(inputLine,'six')<first:
        first=textChecker(inputLine,'six')
        outputLine=inputLine.replace("six","6")
    if textChecker(inputLine,'seven')<first:
        first=textChecker(inputLine,'seven')
        outputLine=inputLine.replace("seven","7")
    if textChecker(inputLine,'eight')<first:
        first=textChecker(inputLine,'eight')
        outputLine=inputLine.replace("eight","8")
    if textChecker(inputLine,'nine')<first:
        first=textChecker(inputLine,'nine')
        outputLine=inputLine.replace("nine","9")
    return outputLine

#compare text number indices and fix the first one (backwards)
def textFixer2(inputLine):
    outputLine=inputLine
    first=textChecker(inputLine,'eno')
    if first < 9999:
        outputLine=inputLine.replace("eno","1")
    if textChecker(inputLine,'owt')<first:
        first=textChecker(inputLine,'owt')
        outputLine=inputLine.replace("owt","2")
    if textChecker(inputLine,'eerht')<first:
        first=textChecker(inputLine,'eerht')
        outputLine=inputLine.replace("eerht","3")
    if textChecker(inputLine,'ruof')<first:
        first=textChecker(inputLine,'ruof')
        outputLine=inputLine.replace("ruof","4")
    if textChecker(inputLine,'evif')<first:
        first=textChecker(inputLine,'evif')
        outputLine=inputLine.replace("evif","5")
    if textChecker(inputLine,'xis')<first:
        first=textChecker(inputLine,'xis')
        outputLine=inputLine.replace("xis","6")
    if textChecker(inputLine,'neves')<first:
        first=textChecker(inputLine,'neves')
        outputLine=inputLine.replace("neves","7")
    if textChecker(inputLine,'thgie')<first:
        first=textChecker(inputLine,'thgie')
        outputLine=inputLine.replace("thgie","8")
    if textChecker(inputLine,'enin')<first:
        first=textChecker(inputLine,'enin')
        outputLine=inputLine.replace("enin","9")
    return outputLine

def intChecker(chr): #this is the int checker, it checks int
    try:
        int(chr)
        return '$'
    except:
        return chr
    
def digitFinder(inputLine):
    #fix the first text number
    frontFixedLine=textFixer(inputLine)

    L=len(frontFixedLine)

    #split line to chars
    chars=list(frontFixedLine[0:L-1])
    print(chars)
    #first digit
    isNum=list(map(intChecker,chars))
    firstDigitIndex=isNum.index('$')
    firstDigit=int(chars[firstDigitIndex])


    #last digit
    
    backFixedLine=textFixer2("".join(reversed(inputLine)))
    L=len(backFixedLine)
    chars2=list(backFixedLine[1:L])
    print(chars2)
    isNum=list(map(intChecker,chars2))
    lastDigitIndex=isNum.index('$')
    lastDigit=int(chars2[lastDigitIndex])


    #combine
    output= (10*firstDigit)+lastDigit
    return output

LOL=list(map(digitFinder,inputWhole)) #lists on lists

print(sum(LOL)) 







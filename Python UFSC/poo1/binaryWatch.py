myHoursBases = [8, 4, 2, 1]

myMinutesBases = [32, 16, 8, 4, 2, 1]

def onWatch(num, myBases):
    if num in myBases:
        return "o"
    else:
        return " "

def myWatch(hoursArr, minutesArr):
    print(" ____________________________________________")
    print("|                                            |")
    print("|    ____________________________________    |_")
    print("|   |                                    |   |_)")
    print("|   |   8         4         2         1  |   |")
    print("|   |                                    |   |")
    print(f"|   |   {onWatch(8, hoursArr)}         {onWatch(4, hoursArr)}         {onWatch(2, hoursArr)}         {onWatch(1, hoursArr)}  |   |")
    print("|   |                                    |   |")
    print("|   |                                    |   |")
    print(f"|   |   {onWatch(32, minutesArr)}     {onWatch(16, minutesArr)}     {onWatch(8, minutesArr)}     {onWatch(4, minutesArr)}     {onWatch(2, minutesArr)}     {onWatch(1, minutesArr)}  |   |")
    print("|   |                                    |   |")
    print("|   |   32    16    8     4     2     1  |   |_")
    print("|   |____________________________________|   |_)")
    print("|                                            |")
    print("|____________________________________________|")
    print("\n")

def isBase(num, base):
    return num >= base

while True:
    hoursBasesResult = []
    minutesBasesResult = []
    try:
        hour, minute = map(int, input().split(':'))
        #hours loop
        for base in range(len(myHoursBases)):
            if isBase(hour, myHoursBases[base]):
                hour -= myHoursBases[base]
                hoursBasesResult.append(myHoursBases[base])

        #minutes loop
        for base in range(len(myMinutesBases)):
            if isBase(minute, myMinutesBases[base]):
                minute -= myMinutesBases[base]
                minutesBasesResult.append(myMinutesBases[base])
        print(hoursBasesResult)
        print(minutesBasesResult)
        myWatch(hoursBasesResult, minutesBasesResult)
    except EOFError:
        break

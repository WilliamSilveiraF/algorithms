while True:
    try:
        toTheMission, toTheHome = map(int, input().split(' '))
        returned = list(map(int, input().split(' ')))
        if toTheMission == toTheHome:
            print("*")
            continue
        inMission = []
        for volunteer in range(1, toTheMission + 1):
            if not(volunteer in returned):
                inMission.append(str(volunteer))
        myStr = ""
        for n in inMission:
            myStr = myStr + n + " "
        print(myStr)
    except EOFError:
        break

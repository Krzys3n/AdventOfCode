def get_directrion(char, lastDir):
    if char == '|':
        if lastDir == 'North':
            return 'North'
        if lastDir == 'South':
            return 'South'
    if char == '-':
        if lastDir == 'West':
            return 'West'
        if lastDir == 'East':
            return 'East'
    if char == 'J':
        if lastDir == 'South':
            return 'West'
        if lastDir == 'East':
            return 'North'
    if char == 'L':
        if lastDir == 'South':
            return 'East'
        if lastDir == 'West':
            return 'North'
    if char == 'F':
        if lastDir == 'North':
            return 'East'
        if lastDir == 'West':
            return 'South'
    if char == '7':
        if lastDir == 'North':
            return 'West'
        if lastDir == 'East':
            return 'South'

with open('input.txt') as f:
    lines = f.readlines()
    print(lines)
    positionX = -1
    positionY = -1
    positionS = []
    for line in lines:
        positionY += 1
        line = line.strip('\n')
        for char in line:
            if char == 'S':
                positionS.append(positionY )
                positionS.append(positionX)
            positionX += 1
        positionX = 0
    print(positionS)
    oldPositionS = positionS
    positionS[0] +=1
    print(positionS)

    lastDir = "South"
    char
    steps = 0
    while char != 'S':
        char = lines[positionS[0]][positionS[1]]
        steps += 1
        print(lastDir)
        print(char)
        if char == '|':
            if lastDir == 'North':
                positionS[0] -= 1
            if lastDir == 'South':
                positionS[0] += 1
        if char == '-':
            if lastDir == 'West':
                positionS[1] -= 1
            if lastDir == 'East':
                positionS[1] += 1
        if char == 'J':
            if lastDir == 'South':
                positionS[1]  -= 1
            if lastDir == 'East':
                positionS[0]  -= 1
        if char == 'L':
            if lastDir == 'South':
                positionS[1] += 1
            if lastDir == 'West':
                positionS[0] -= 1
        if char == 'F':
            if lastDir == 'North':
                positionS[1] += 1
            if lastDir == 'West':
                positionS[0] += 1
        if char == '7':
            if lastDir == 'North':
                positionS[1] -= 1
            if lastDir == 'East':
                positionS[0] += 1
        lastDir = get_directrion(char, lastDir)
    if steps % 2 == 1:
        steps -= 1
        steps/=2
    else:
        steps /= 2
    print(int(steps))
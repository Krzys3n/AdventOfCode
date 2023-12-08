with open('input.txt') as file:
    instructions = file.readline()
    map_instructions = {}
    for line in file:
        map_instructions[line[0:3]] = [line[7:10],line[12:15]]
    print(map_instructions)
    position = 'AAA'
    i = 0
    steps = 0
    while position != 'ZZZ':
        if i == len(instructions)-1:
            i = 0
        direction = instructions[i]
        print("Direction: ", direction)
        if direction == "R":
            position = map_instructions[position][1]
        elif direction == "L":
            position = map_instructions[position][0]
        print(position)


        i += 1
        steps += 1
        # if steps == 50:
        #     break

    print(steps)
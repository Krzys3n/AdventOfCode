import math

with open('input.txt') as file:
    instructions = file.readline()
    map_instructions = {}
    starting_positions = []
    for line in file:
        position = line[0:3]
        map_instructions[line[0:3]] = [line[7:10],line[12:15]]
        if line[2] == 'A':
            starting_positions.append(position)
    print(map_instructions)
    print(starting_positions)
    position = '11A'
    steps_list = []
    for y in range(0, len(starting_positions)):
        i = 0
        steps = 0
        while starting_positions[y][2] != 'Z':
            if i == len(instructions)-1:
                i = 0
            direction = instructions[i]
            if direction == "R":
                starting_positions[y] = map_instructions[starting_positions[y]][1]
            elif direction == "L":
                starting_positions[y] = map_instructions[starting_positions[y]][0]
            # print("Direction: ", direction," Position: ",starting_positions[y])

            i += 1
            steps += 1
            # if steps == 50:
            #     break
        print(starting_positions)
        print(steps)
        steps_list.append(steps)
print(math.lcm(*steps_list))
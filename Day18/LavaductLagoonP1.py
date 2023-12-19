

with open("input.txt") as f:
    dig_plan = f.readlines()
    print(dig_plan)
    coords = []
    coord = [0, 0]
    # coords.append(coord.copy())
    sum_of_distance = 0
    for line in dig_plan:

        line = line.split()


        direction = line[0]
        distance = int(line[1])


        sum_of_distance += distance
        if direction == "R":

            coord[1] = coord[1] + distance

        elif direction == "L":

            coord[1] = coord[1] - distance

        elif direction == "U":

            coord[0] = coord[0] - distance

        elif direction == "D":
            coord[0] = coord[0] + distance

        coords.append(coord.copy())


    sum_area = 0.0

    for n in range(len(coords)-1 ):
        part = coords[n][1] * coords[n + 1][0] - coords[n][0] * coords[n + 1][1]
        sum_area += part


    x1, y1 = coords[-1]
    x2, y2 = coords[0]
    sum_area += (x1 * y2 - x2 * y1)

    sum_area = abs(sum_area) / 2.0
    print(sum_area)
    i = sum_of_distance /2 + 1
    print(i)
    print(i+sum_area)

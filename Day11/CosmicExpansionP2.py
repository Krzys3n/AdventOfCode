def get_pairs(x):
    if x-1 == 1:
        return 1
    else:
        return x-1 + get_pairs(x - 1)

print(get_pairs(9))

def expand_cosmos(cosmos,galaxies_coords):
    i = 0
    expansion = 999999
    cosmos
    gc = [list(coord) for coord in galaxies_coords]

    for y in range(0,len(cosmos)):
        if all(cosmos[y][x] == '.' for x in range(len(cosmos[y]))):
            print(y, cosmos[y])
            for coord_index in range(0,len(galaxies_coords)):
                if galaxies_coords[coord_index][0] > y:
                    gc[coord_index][0] = gc[coord_index][0] + expansion

    cosmos = [''.join(row) for row in zip(*cosmos[::-1])]


    for g in cosmos:
        print(g)
    print(gc)
    for z in range(0,len(cosmos)):
        if all(cosmos[z][x] == '.' for x in range(len(cosmos[x]))):
            print(z, cosmos[z])
            for coord_index in range(0, len(galaxies_coords)):
                if galaxies_coords[coord_index][1] > z:
                    gc[coord_index][1] = gc[coord_index][1] + expansion
    print(gc)
    return gc


with open('input.txt') as f:
    cosmos = f.readlines()
    cosmos = [x.strip() for x in cosmos]
    galaxy_coords = []
    for y in range(0, len(cosmos)):
        for x in range(0, len(cosmos[y])):
            if cosmos[y][x] == '#':
                galaxy_coords.append((y,x))
    for g in cosmos:
        print(g)
    print(galaxy_coords)
    # print(expand_cosmos(cosmos,galaxy_coords))
    galaxy_coords = expand_cosmos(cosmos,galaxy_coords)
    path = 0
    for i in range(0, (len(galaxy_coords))):
        for y in range(i + 1, len(galaxy_coords)):
            path += abs(galaxy_coords[i][0] - galaxy_coords[y][0]) + abs(galaxy_coords[i][1] - galaxy_coords[y][1])
    print(path)


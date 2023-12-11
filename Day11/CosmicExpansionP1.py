def get_pairs(x):
    if x-1 == 1:
        return 1
    else:
        return x-1 + get_pairs(x - 1)

print(get_pairs(9))

def expand_cosmos(cosmos):
    i = 0
    new_cosmos = cosmos.copy()
    for galaxy in cosmos:
        if all(galaxy[x] == '.' for x in range(len(galaxy))):
            # print(i,galaxy)
            new_cosmos.insert(i, '.' * len(galaxy))
            i+=1
        i += 1
    new_cosmos = [''.join(row) for row in zip(*new_cosmos)]
    i = 0
    new_cosmos2 = new_cosmos.copy()
    for galaxy in new_cosmos:
        if all(galaxy[x] == '.' for x in range(len(galaxy))):
            # print(i,galaxy)
            new_cosmos2.insert(i, '.' * len(galaxy))
            i+=1
        i += 1
    new_cosmos2 = [''.join(row) for row in zip(*new_cosmos2)]
    return new_cosmos2

with open('input_example.txt') as f:
    cosmos = f.readlines()
    cosmos = [x.strip() for x in cosmos]
    cosmos = expand_cosmos(cosmos)
    galaxy_coords = []
    for y in range(0, len(cosmos)):
        for x in range(0, len(cosmos[y])):
            if cosmos[y][x] == '#':
                galaxy_coords.append((y,x))
    for galaxy in cosmos:
        print(galaxy)
    print(galaxy_coords)
    z = 1
    path = 0
    for i in range(0,(len(galaxy_coords))):
        for y in range(i+1,len(galaxy_coords)):
            path += abs(galaxy_coords[i][0] - galaxy_coords[y][0]) + abs(galaxy_coords[i][1] - galaxy_coords[y][1])
            print(path)

            # print(z, ' ', end='')
            # print(galaxy_coords[i], ' ', end='')
            # print (galaxy_coords[y],' ',end='')
            # z+=1


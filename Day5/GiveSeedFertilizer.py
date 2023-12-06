
data = {}


with open('Almanac_example.txt', 'r') as file:
    seeds = file.readline().strip().split()[1:]
    print("Seeds: ", seeds)
    current_key = None
    current_values = []

    for line in file:
        line = line.strip()

        if line and ord(line[0]) > 57:
            # This line is a header line
            if current_key is not None:
                data[current_key] = current_values
            current_key = line
            current_values = []
        elif line:
            values = list(map(int, line.split()))
            current_values.append(values)


    if current_key is not None:
        data[current_key] = current_values


location = 0
locationmin = 9999999999999999999999999999999999999
for seed in seeds:
    location = int(seed)
    print("Seed: ", seed)

    for key, valuesall in data.items():
        for values in valuesall:
            destination =int(values[0])
            source = int(values[1])
            rangex =int(values[2])
            if source <= location <= source+ rangex:
                location = location + destination - source
                break
            # print("Destination: ", destination)
            # print("Source: ", source)
            # print("Range: ", range)
            # print("Location: ", location)
            # print("-----------------------")
    if location < locationmin:
        locationmin = location
        break
    print("Location: ", location)
print("Minimum location: ", locationmin)


data = {}

with open('Almanac.txt', 'r') as file:
    seeds = file.readline().strip().split()[1:]
    print("Seeds: ", seeds)
    current_key = None
    current_values = []
    #wczytywanie danych do słownika
    for line in file:
        line = line.strip()

        if line and ord(line[0]) > 57:
            if current_key is not None:
                data[current_key] = current_values
            current_key = line
            current_values = []
        elif line:
            values = list(map(int, line.split()))
            current_values.append(values)

    if current_key is not None:
        data[current_key] = current_values

        # tu się dzieje cała magia
minimum_location_value_seed = 0
location = 0
location_min = 9999999999999999999999999999999999999
for seed_ranges in range(0, len(seeds) - 1, 2):
    rangeStart = int(seeds[seed_ranges])
    rangeEnd = int(seeds[seed_ranges]) + int(seeds[seed_ranges + 1])
    for seed in range(rangeStart, rangeEnd, 100000):
        location = seed
        for key, valuesall in data.items():
            for values in valuesall:
                destination = int(values[0])
                source = int(values[1])
                rangex = int(values[2])
                if source <= location <= source + rangex:
                    location = location + destination - source
                    break
        print("Location for seed: ", seed, ":", location)
        if location < location_min and seed<rangeEnd :
            minimum_location_value_seed = seed
            location_min = location
            minimum_location_seed_range = seeds[seed_ranges] + " " + seeds[seed_ranges + 1]

    for seed in range(minimum_location_value_seed-10000, minimum_location_value_seed+10000, 1):
        location = seed
        for key, valuesall in data.items():
            for values in valuesall:
                destination = int(values[0])
                source = int(values[1])
                rangex = int(values[2])
                if source <= location <= source + rangex:
                    location = location + destination - source
                    break
        print("Location for seed: ", seed, ":", location)
        if location < location_min and seed < rangeEnd:
            minimum_location_value_seed = seed
            location_min = location
            minimum_location_seed_range = seeds[seed_ranges] + " " + seeds[seed_ranges + 1]

print("Minimum location: ", location_min)
print("Minimum location seed: ", minimum_location_value_seed)
print("Minimum location seedrange : ", minimum_location_seed_range)

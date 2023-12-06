with open("input.txt") as file:
    times = file.readline().split()[1:]
    times = ''.join(times)
    # time = time[1:]
    print(times)
    records = file.readline().split()[1:]
    records = ''.join(records)
    print(records)
    allways = 1
    # for time,record in zip(times,records):
    ways = 0
    maximum_holding = 0
    minimum_holding = 999999999999999999999999
    for holding_button_time in range(6863000-1000,33965000+1000,1):
        distance =int(holding_button_time) * (int(times)-int(holding_button_time))

        if distance > int(records):
            ways+=1
            if holding_button_time < minimum_holding:
                minimum_holding = holding_button_time
            if holding_button_time > maximum_holding:
                maximum_holding = holding_button_time

            # print('holding button time: ',holding_button_time)
            # print("distance: ", distance)
    print('minimum holding: ', minimum_holding)
    print('maximum holding: ', maximum_holding)
    allways = allways * ways
print(allways)
    # dokladnosc 1000: 27103
    # dokładność 100: 271028


with open("input.txt") as file:
    times = file.readline().split()[1:]
    # time = time[1:]
    print(times)
    records = file.readline().split()[1:]
    print(records)
    allways = 1
    for time,record in zip(times,records):
        ways = 0
        for holding_button_time in range(0,int(time)+1):
            distance =int(holding_button_time) * (int(time)-int(holding_button_time))

            if distance > int(record):
                ways+=1
                print('holding button time: ',holding_button_time)
                print("distance: ", distance)
        allways = allways * ways
    print(allways)




if __name__ == '__main__':
    # wczytywanie pliku
    with open('input.txt', 'r') as file:
        last_line  = file.readline()
        current_line = file.readline()
        number = ''
        sum_of_gears = 0
        numbers = []
        found_number = False
        for next_line in file:
            for i in range(len(current_line)):
                if(current_line[i] == "*"):
                    found_number = False
                    #   ...
                    #   x*.
                    #   ...
                    if i - 1 >= 0 and current_line[i - 1].isdigit():
                        y=i-1
                        while(current_line[y].isdigit()== True):
                            number = current_line[y] + number
                            y-=1
                        numbers.append(int(number))
                        number = ''
                    #   ...
                    #   .*x
                    #   ...
                    if i + 1 < len(current_line) - 1 and current_line[i + 1].isdigit():
                        y = i + 1
                        while(current_line[y].isdigit() == True):
                            number = number + current_line[y]
                            y+=1
                        numbers.append(int(number))
                        number = ''
                    #   .x.
                    #   .*.
                    #   ...
                    if last_line[i].isdigit() == True:
                        found_number = True
                        number = last_line[i]
                        y = i-1
                        while (last_line[y].isdigit() == True):
                            number = last_line[y] + number
                            y -= 1
                        y = i + 1
                        while (last_line[y].isdigit() == True):
                            number = number + last_line[y]
                            y += 1
                        numbers.append(int(number))
                        number = ''
                    #   x..
                    #   .*.
                    #   ...
                    if i - 1 >= 0 and last_line[i - 1].isdigit() and found_number ==False:
                        y = i - 1
                        while (last_line[y].isdigit() == True):
                            number = last_line[y] + number
                            y -= 1
                        numbers.append(int(number))
                        number = ''
                        found_number == False
                    #   ..x
                    #   .*.
                    #   ...
                    if i + 1 < len(last_line) - 1 and last_line[i + 1].isdigit() and found_number ==False:
                        y = i + 1
                        while (last_line[y].isdigit() == True):
                            number = number + last_line[y]
                            y += 1
                        numbers.append(int(number))
                        number = ''
                        found_number = False
                    found_number = False
                    #   ...
                    #   .*.
                    #   .x.
                    if next_line[i].isdigit() == True:
                        found_number = True
                        number = next_line[i]
                        y = i - 1
                        while (next_line[y].isdigit() == True):
                            number = next_line[y] + number
                            y -= 1
                        y = i + 1
                        while (next_line[y].isdigit() == True):
                            number = number + next_line[y]
                            y += 1
                        numbers.append(int(number))
                        number = ''
                    #   ...
                    #   .*.
                    #   x..
                    if i - 1 >= 0 and next_line[i - 1].isdigit() and found_number == False:
                        y = i - 1
                        while (next_line[y].isdigit() == True):
                            number = next_line[y] + number
                            y -= 1
                        numbers.append(int(number))
                        number = ''
                        found_number == False
                    #   ...
                    #   .*.
                    #   ..x
                    if i + 1 < len(next_line) - 1 and next_line[i + 1].isdigit() and found_number == False:
                        y = i + 1
                        while (next_line[y].isdigit() == True):
                            number = number + next_line[y]
                            y += 1
                        numbers.append(int(number))
                        number = ''
                        found_number = False
                    found_number = False
                if (0<len(numbers) < 2):
                    print(numbers)
                if(len(numbers)==2):
                    print(numbers)
                    # print(len(numbers))
                    sum_of_gears += numbers[0] * numbers[1]
                numbers = []
            number = ''
            # print(last_line)
            # print(actual_line)
            # print(next_line)
            print("-------------------------")
            last_line = current_line
            current_line = next_line

        print("Sum of gears is: ", sum_of_gears)
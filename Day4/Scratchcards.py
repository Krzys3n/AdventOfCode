import re

if __name__ == '__main__':
    # wczytywanie pliku
    with open('input.txt', 'r') as file:

        separators = [":", "|", "\n"]
        power = -1
        sum_of_power = 0
        for line in file:
            line = [re.split('|'.join(map(re.escape, separators)), line)]
            print(line)
            game_id = line[0][0][5]
            winning_numbers = line[0][1].split()
            numbers_you_have = line[0][2].split()
            print(winning_numbers)
            print(numbers_you_have)
            for number_you_have in numbers_you_have:
                for winning_number in winning_numbers:
                    if winning_number in winning_numbers:
                        if winning_number == number_you_have:
                            power += 1
                            print(winning_number)
            print(power)
            if power > -1:
                sum_of_power = sum_of_power +pow(2,power)
            power = -1
        print(sum_of_power)


if __name__ == '__main__':
    # wczytywanie pliku
    with open('input.txt', 'r') as file:
        last_line  = file.readline()
        current_line = file.readline()
        number = ''
        has_an_adjacent_symbol = False
        sum_of_codes = 0
        for next_line in file:
            for i in range(len(current_line)):
                if(current_line[i].isdigit()):
                    number += current_line[i]
                    if (
                            (i - 1 >= 0 and current_line[i - 1] != '.' and not current_line[i - 1].isdigit()) or
                            (i + 1 < len(current_line) - 1 and current_line[i + 1] != '.' and not current_line[
                                i + 1].isdigit()) or
                            (i - 1 >= 0 and last_line[i - 1] != '.' and not last_line[i - 1].isdigit()) or
                            (i + 1 < len(last_line) - 1 and last_line[i + 1] != '.' and not last_line[
                                i + 1].isdigit()) or
                            (i - 1 >= 0 and last_line[i] != '.' and not last_line[i].isdigit()) or
                            (i + 1 < len(last_line) - 1 and last_line[i + 1] != '.' and not last_line[
                                i + 1].isdigit()) or
                            (i - 1 >= 0 and next_line[i - 1] != '.' and not next_line[i - 1].isdigit()) or
                            (i + 1 < len(next_line) - 1 and next_line[i + 1] != '.' and not next_line[
                                i + 1].isdigit()) or
                            (i - 1 >= 0 and next_line[i] != '.' and not next_line[i].isdigit()) or
                            (i + 1 < len(next_line) - 1 and next_line[i + 1] != '.' and not next_line[i + 1].isdigit())
                    ):
                        has_an_adjacent_symbol = True

                    if(current_line[i+1].isdigit() ==False):
                        print(number)
                        print(has_an_adjacent_symbol)
                        if(has_an_adjacent_symbol == True):
                            sum_of_codes += int(number)
                        number = ''
                        has_an_adjacent_symbol = False;
            # print(liczba)
            number = ''
            # print(last_line)
            # print(actual_line)
            # print(next_line)
            print("-------------------------")
            last_line = current_line
            current_line = next_line
        print("Sum of codes is: ", sum_of_codes)
if __name__ == '__main__':
    digits_names = ['*', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    with open('input1.txt', 'r') as file:
        sum = 0
        for line in file:

            digits = [None] * len(line)
            for digit in digits_names:
                start_index = 0
                while True:
                    index = line.find(digit, start_index)
                    if index == -1:
                        break
                    if index + len(digit) <= len(digits):
                        digit_index = digits_names.index(digit)
                        if digits_names.index(digit)>9:
                            digit_index -=9

                        digits[index] = digit_index
                    start_index = index + 1

            digits = list(filter(lambda x: x is not None, digits))

            if(len(digits) == 1 ):
                s = str(digits[0])+str(digits[0])
                sum+=int(s)
            elif(len(digits) > 1):
                s =str(digits[0]) + str(digits[-1])
                sum+=int(s)
        print(sum)

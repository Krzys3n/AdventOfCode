import re

if __name__ == '__main__':
    # wczytywanie pliku
    with open('input.txt', 'r') as file:
        card_dict = {f'Card {i}': 1 for i in range(1, 204)}
        sum = 0
        separators = [":", "|", "\n"]
        power = -1
        sum_of_power = 0
        sum_of_games = 0
        for line in file:
            line = [re.split('|'.join(map(re.escape, separators)), line)]
            game_id = int(line[0][0].split()[1])

            print("gameid",game_id)
            winning_numbers = line[0][1].split()
            numbers_you_have = line[0][2].split()
            for number_you_have in numbers_you_have:
                for winning_number in winning_numbers:
                    if winning_number in winning_numbers:
                        if winning_number == number_you_have:
                            power += 1
            print("power",power+1)

            for i in range(game_id+1,game_id + power+2):
                if game_id == 1:
                    card_dict[f'Card {i}'] = card_dict[f'Card {i}'] + 1
                if game_id > 1:
                    card_dict[f'Card {i}'] =card_dict[f'Card {i}']+card_dict[f'Card {game_id}']
                print(card_dict)
            if power > -1:
                sum_of_power = sum_of_power +pow(2,power)
            power = -1

        print(sum_of_power)
        print(card_dict)
        for i in card_dict:
            sum_of_games = sum_of_games + card_dict[i]
    print('sum of games', sum_of_games)


import re


class Game():
    # pola klasy
    id_game = 0
    info = []
    bag_bound = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    # inicjalizator klasy
    def __init__(self, bag_bound, game_info):
        self.bag_bound = bag_bound
        Game.id_game += 1
        self.id_game = Game.id_game
        self.info = game_info[1:-1]
        self.bag = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        self.power = 0;
    # funkcja do liczenia kostek każdego koloru z informacji z pliku i do aktualizowana mocy każdego zestawu
    def update_bag(self):
        for item in self.info:
            count, color = item.strip().split()
            count = int(count)
            if(count > self.bag[color]):
                self.bag[color] = count
        self.power = self.bag[ 'red']*self.bag[ 'green']*self.bag[ 'blue']
    # funkcja do sprawdzania czy ograniczenia zostały przekroczone
    def is_out_of_bounds(self):
        if (self.bag['red'] <= bag_bound['red'] and self.bag['green'] <= bag_bound['green'] and self.bag['blue'] <=
                bag_bound['blue']):
            return False
        else:
            return True
    

if __name__ == '__main__':
    # wczytywanie pliku
    with open('games.txt', 'r') as file:
        # ustawianie ograniczeń dla zadania
        bag_bound = {
            'red': 12,
            'green': 13,
            'blue': 14
        }
        # inicjalizacja sumy indeksów
        sum_of_indexes = 0
        sum_of_power = 0
        # iterowanie przez plik
        for game_info in file:
            # dzielenie informacji na potrzebne części
            game_info = re.split(r'[:,;,\n]', game_info)
            # tworzenie instancji gry
            game = Game(bag_bound, game_info)
            game.update_bag()
            print(game.id_game, game.bag)
            print(game.is_out_of_bounds())
            # aktualizowanie sumy zależnie od wyniku gry
            if (game.is_out_of_bounds() == False):
                sum_of_indexes += game.id_game
            sum_of_power += game.power
            print('Power: ', game.power)

        print('sum of indexes: ', sum_of_indexes)
        print('sum of power: ',sum_of_power)


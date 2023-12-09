with open("input.txt") as f:
    input = f.read().splitlines()
    steps = 0
    print(input)
    Oasis = 0
    for history in input:
        list_of_history = []
        history = list(map(int, history.split()))
        list_of_history.append(history.copy())
        while any(data != 0 for data in history):

            for i in range(len(history) - 1):
                history[i] = history[i + 1] - history[i]

            history = history[:-1]

            list_of_history.append(history.copy())
        list_of_history.reverse()

        for i in range(1, len(list_of_history)):
            list_of_history[i].append(list_of_history[i - 1][-1] + list_of_history[i][-1])
        Oasis += list_of_history[-1][-1]
    print(Oasis)

score = {'R': 1, 'P': 2, 'S': 3}
win = {'R': 'S', 'P': 'R', 'S': 'P'}
lose = {'R':'P','P':'S','S':'R'}
trans = {
    'A': 'R', 'B': 'P', 'C': 'S',
    'X': 'R', 'Y': 'P', 'Z': 'S',
}

def solve1(input):
    result = 0
    with open(input) as f:
        players_list = f.read().split('\n')
        for players in players_list:
            players = players.split()
            A, B= trans[players[0]], trans[players[1]]
            if A == B:
                result += 3
            elif win[B] == A:
                result += 6
            result += score[B]
        return result

def solve2(input):
    result = 0
    with open(input) as f:
        players_list = f.read().split('\n')
        for players in players_list:
            players = players.split()
            A, B= trans[players[0]], players[1]
            if B == 'X':
                result += score[win[A]]
            elif B == 'Y':
                result += (3 + score[A])
            elif B == 'Z':
                result += (6 + score[lose[A]])
        return result
if __name__ == "__main__":
    print(solve1("./input.txt"), solve2("./input.txt"))
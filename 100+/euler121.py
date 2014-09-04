from itertools import combinations

def euler121():
    turns = 15
    max_losses = (turns) - (turns / 2 + 1)
    red_picks = []
    
    for i in range(1, max_losses+1):
        for picks in combinations(range(1, turns+1), i):
            red_picks.append(picks)

    ways_to_win = [1]*len(red_picks)
    for idx, picks in enumerate(red_picks):
        for pick in picks:
            ways_to_win[idx] *= pick

    return reduce(lambda x,y: x*y, range(2, turns+2)) / (sum(ways_to_win)+1)

if __name__ == "__main__":
    print euler121()

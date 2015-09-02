def get_games():
    f = open("p054_poker.txt", "r")
    games = f.read().split("\n")
    return [game.split() for game in games][:-1]

def get_val(hand):
    card_val = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    
    suits = [card[1] for card in hand]
    vals = [card[0] for card in hand]
    high_val = max([card_val[val] for val in vals])
    low_val = min([card_val[val] for val in vals])
    
    flush = (len(set(suits)) == 1)
    straight = (high_val - low_val == 4 and len(set(vals)) == 5)

    if flush and straight: return 160 + high_val

    counts = {}
    for val in vals: counts[val] = 0
    for val in vals: counts[val] += 1

    pair_max = 0
    three_found, two_found = False, False
    three_key, two_key = '', ''
    for key in counts.keys():
        #4 of a kind
        if counts[key] == 4: return 140 + card_val[key]

        # 3 of a kind
        if counts[key] == 3:
            if two_found: return 120 + card_val[key]
            pair_max = 60 + card_val[key]
            three_found, three_key = True, key

        # pair
        if counts[key] == 2:
            if three_found: return 120 + card_val[three_key]
            elif two_found:
                kicker = min(card_val[key], card_val[two_key]) / 10.0
                pair_max = 40 + max(card_val[key], card_val[two_key]) + kicker
            else: pair_max = 20 + card_val[key]
            two_found, two_key = True, key

    if flush: return 100 + high_val
    if straight: return 80 + high_val

    if pair_max > 0: return pair_max
    else: return high_val

def tie_break(game):
    card_val = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    
    p1_hand = game[:5]
    p2_hand = game[5:]
    p1_vals = [card[0] for card in p1_hand]
    p2_vals = [card[0] for card in p2_hand]
    p1_tmp = []
    p2_tmp = []

    for card1, card2 in zip(p1_vals, p2_vals):
        count = p1_vals.count(card1)
        if count == 1: p1_tmp.append(card1)
        count = p2_vals.count(card2)
        if count == 1: p2_tmp.append(card2)

    for p1, p2 in zip(sorted(p1_tmp)[::-1], sorted(p2_tmp)[::-1]):
        if card_val[p1] > card_val[p2] + 0.01: return 1
        elif card_val[p1] + 0.01 < card_val[p2]: return 2

    return -1

def play_game(game):
    p1_val = get_val(game[:5])
    p2_val = get_val(game[5:])
    if p1_val - 0.0001 < p2_val < p1_val + 0.0001: return tie_break(game)
    elif p1_val > p2_val: return 1
    elif p1_val < p2_val: return 2
    else: return -1
    

def euler54():
    p1_wins = 0
    games = get_games()
    
    for game in games:
        winner = play_game(game)
        if winner == 1: p1_wins += 1

    return p1_wins

if __name__ == "__main__":
    print euler54()

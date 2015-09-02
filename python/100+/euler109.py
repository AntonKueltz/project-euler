singles = range(1, 21)+[25]
doubles = [2*i for i in singles]
triples = [3*i for i in range(1, 21)]

def checkouts(rem):
    ways = 0
    if rem > 170: return ways

    for dd in doubles:
        # one shot
        if rem == dd:
            ways += 1
            continue

        # two shots
        shot_two = rem-dd
        if shot_two <= 0: continue
        if shot_two in singles: ways += 1
        if shot_two in doubles: ways += 1
        if shot_two in triples: ways += 1

        # three shots
        for t in triples:
            shot_one = shot_two-t
            if shot_one <= 0: continue
            if shot_one in triples and shot_one <= t: ways += 1
            if shot_one in doubles: ways += 1
            if shot_one in singles: ways += 1

        for d in doubles:
            shot_one = shot_two-d
            if 50 < shot_one <= 0: continue
            if shot_one in doubles and shot_one <= dd: ways += 1
            if shot_one in singles: ways += 1

        for s in singles:
            shot_one = shot_two-s
            if 25 < shot_one <= 0: continue
            if shot_one in singles and shot_one <= s: ways += 1
        
    return ways
        
def euler109():
    return sum(map(checkouts,range(1, 100)))

if __name__ == "__main__":
    print euler109()

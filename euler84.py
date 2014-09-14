import random

# special space constants
jail, go, g2j = 10, 0, 30
cc, ch = (2, 17, 33), (7, 22, 36)

# spaces chance can send you to
c1, e3, h2, r1 = 11, 24, 39, 5

def roll():
    die1 = random.randint(1, 4)
    die2 = random.randint(1, 4)
    return (die1+die2, die1==die2)

def chance(cur_space):
    card = random.randint(1, 16)
    if card == 1: return go
    elif card == 2: return jail
    elif card == 3: return c1
    elif card == 4: return e3
    elif card == 5: return h2
    elif card == 6: return r1
    elif card == 7 or card == 8:
        if 5 > cur_space or cur_space > 35: return 5
        elif 15 > cur_space > 5: return 15
        elif 25 > cur_space > 15: return 25
        elif 35 > cur_space > 25: return 35
    elif card == 9:
        if 28 > cur_space > 12: return 28
        elif 28 < cur_space or cur_space < 12: return 12
    elif card == 10: return cur_space-3
    else: return cur_space

def community_chest(cur_space):
    card = random.randint(1, 16)
    if card == 1: return go
    elif card == 2: return jail
    else: return cur_space

def top_three(arr):
    top, copy = [], []
    for a in arr: copy.append(a)
    
    for i in range(3):
        tmp = max(copy) 
        top.append(arr.index(tmp))
        copy.remove(tmp)
    return top

def euler84():
    space_visits = [0]*40
    rolls, cur_space = 0, 0
    dubs_in_row = 0

    # run 100000 turns and see which spaces were visited the most
    while rolls < 100000:
        space_visits[cur_space] += 1
        
        cur_roll, doubles = roll()
        if doubles: dubs_in_row += 1
        else: dubs_in_row = 0
        
        if dubs_in_row == 3 or cur_space + cur_roll % 40 == g2j:
            cur_space = jail
            continue

        cur_space = (cur_space + cur_roll) % 40
        
        if cur_space in cc: cur_space = community_chest(cur_space)
        elif cur_space in ch: cur_space = chance(cur_space)

        rolls += 1

    return top_three(space_visits)

if __name__ == "__main__":
    print euler84()

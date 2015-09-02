def read_in_puzzles():
    f = open("p096_sudoku.txt", "r")
    lines = f.read().split("\n")

    puzzles = []
    puzzle = []
    for i, line in enumerate(lines):
        if line[:4] == "Grid":
            puzzle = []
        else:
            puzzle.append([int(c) for c in line])
            if i % 10 == 9:
                puzzles.append(puzzle)

    return puzzles

def rowcol_elim(puzzle, row, col, not_in_box):
    for val in list(not_in_box):
        can_go_elsewhere = False
        
        for i in range((row/3)*3, (row/3)*3+3):
            for j in range((col/3)*3, (col/3)*3+3):
                if (i, j) == (row, col): continue
                if puzzle[i][j] != 0: continue
                if val in puzzle[i]: continue

                column = []
                for k in range(len(puzzle)):
                    column.append(puzzle[k][j])
                if val in column: continue

                can_go_elsewhere = True

        if not can_go_elsewhere: return val
    return 0    

def solve_square(puzzle, row, col, backtrack=False):
    tmp = []
    for i in range(len(puzzle[row])):
        if puzzle[row][i] != 0: tmp.append(puzzle[row][i])
    not_in_row = set(range(1,10)).difference(set(tmp))

    tmp = []
    for i in range(len(puzzle)):
        if puzzle[i][col] != 0: tmp.append(puzzle[i][col])
    not_in_col = set(range(1,10)).difference(set(tmp))

    tmp = []
    for i in range((row/3)*3, (row/3)*3+3):
        for j in range((col/3)*3, (col/3)*3+3):
            if puzzle[i][j] != 0: tmp.append(puzzle[i][j])
    not_in_box = set(range(1,10)).difference(set(tmp))

    candidates = not_in_row.intersection(not_in_col.intersection(not_in_box))
    if backtrack: return list(candidates)
    if len(candidates) == 1: return list(candidates)[0]
    else: return rowcol_elim(puzzle, row, col, not_in_box)

def valid(puzzle, row, col, val):
    column = []
    for i in range(len(puzzle)):
        if i != row: column.append(puzzle[i][col])

    row_ = []
    for i in range(len(puzzle[row])):
        if i != col: row_.append(puzzle[row][i])

    box = []
    for i in range((row/3)*3, (row/3)*3+3):
        for j in range((col/3)*3, (col/3)*3+3):
            if (i, j) != (row, col): box.append(puzzle[i][j])
    
    return (not val in row_) and \
           (not val in column) and \
           (not val in box)

def validpuzzle(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0: return False
            if not valid(puzzle, i, j, puzzle[i][j]): return False
    return True

def backtrack(puzzle):
    if validpuzzle(puzzle): return puzzle

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for val in range(1,10):
                    if valid(puzzle, i, j, val):
                        puzzle[i][j] = val
                        solved = backtrack(puzzle)
                        if solved != None: return solved
                        else: puzzle[i][j] = 0
                        
                return None

def solve(puzzle):
    solved = False
    puzzle_before_guess = []
    
    while not solved:
        prev_round = [[i for i in row] for row in puzzle]
        solved = True
        
        for row in range(len(puzzle)):
            for col in range(len(puzzle[row])):
                if puzzle[row][col] == 0:
                    solved = False
                    val = solve_square(puzzle, row, col)
                    puzzle[row][col] = val

        # shortcut
        if(puzzle[0][0] != 0 and puzzle[0][1] != 0 and puzzle[0][2] != 0):
            return

        # puzzle solution cannot be logically deduced, do brute force :(  
        if prev_round == puzzle and not solved:
            backtrack(puzzle)
            return

def euler96():
    puzzles = read_in_puzzles()
    assert(len(puzzles) == 50)
    acc = 0

    for puzzle in puzzles:
        solve(puzzle)
        acc += (100*puzzle[0][0] + 10*puzzle[0][1] + puzzle[0][2])

    return acc

if __name__ == "__main__":
    print euler96()

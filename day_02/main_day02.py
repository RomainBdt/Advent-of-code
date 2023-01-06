# %%
import pathlib


def parse(path):
    """Parse input."""
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


def part1(data):
    """Solve part 1."""
    total_score = 0
    wining_combination = ['A Y', 'B Z', 'C X']
    losing_combination = ['A Z', 'B X', 'C Y']
    for i in data:
        if i in wining_combination:
            total_score += 6
        elif i in losing_combination:
            pass
        else:
            total_score += 3
        
        if i[-1] == "X":
            total_score += 1
        elif i[-1] == "Y":
            total_score += 2
        else:
            total_score += 3
            
    return total_score


def part2(data):
    """Solve part 2."""
    total_score = 0
    for i in data:
        player_1 = i[0]
        strategy = i[-1]  # X: lose, Y: draw, Z:win
        
        if strategy == 'Y':
            total_score += 3
            if player_1 == 'A':
                total_score += 1
            elif player_1 == 'B':
                total_score += 2
            else:
                total_score += 3
                
        elif strategy == 'Z':
            total_score += 6
            if player_1 == 'A':
                total_score += 2
            elif player_1 == 'B':
                total_score += 3
            else:
                total_score += 1
        else:
            if player_1 == 'A':
                total_score += 3
            elif player_1 == 'B':
                total_score += 1
            else:
                total_score += 2
    return total_score
            
            


def solve(path):
    """Solve the puzzle for the given input."""
    data = parse(path)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    path = pathlib.Path.cwd() / "day_02" / "input.txt"
    solution1, solution2 = solve(path)

# %%

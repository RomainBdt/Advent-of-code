# %%
import pathlib


def parse(path):
    """Parse input."""
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


def part1(data):
    """Solve part 1."""
    max_value = 0
    temp = 0
    for i in data:
        if i == "":
            max_value = max(temp, max_value)
            temp = 0
        else:
            temp += int(i)
    return max_value


def part2(data):
    """Solve part 2."""
    temp = 0
    elves_carrying_list = []
    for i in data:
        if i == "":
            elves_carrying_list.append(temp)
            temp = 0
        else:
            temp += int(i)
    elves_carrying_list.sort()
    return sum(elves_carrying_list[-3:])


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    path = pathlib.Path.cwd() / "input_1.txt"
    data = parse(path)

# %%

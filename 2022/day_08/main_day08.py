# %%
import pathlib


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)

grid = [[int(num) for num in line] for line in data]
grid

cnt = 0
for row in range(1, len(grid[0]) - 1):
    for col in range(1, len(grid[0]) - 1):
        num = grid[row][col]
        col_list = [val[col] for val in grid]

        if num > max(grid[row][:col]):
            cnt += 1
            print(num, row, col, "from left")
        elif num > max(grid[row][col + 1 :]):
            cnt += 1
            print(num, row, col, "from right")
        elif num > max(col_list[:row]):
            cnt += 1
            print(num, row, col, "from top")
        elif num > max(col_list[row + 1 :]):
            cnt += 1
            print(num, row, col, "from bottom")
cnt += (len(grid[0]) - 1) * 4
print("PART 1 : ", cnt)

# %%
cnt = 0
max_scenic_score = 0
for row in range(1, len(grid[0]) - 1):
    for col in range(1, len(grid[0]) - 1):
        num = grid[row][col]
        col_list = [val[col] for val in grid]

        left_score = 0
        # look left
        for i in reversed(range(col)):
            left_score += 1
            if grid[row][i] < num:
                continue
            else:
                break

        right_score = 0
        right_view = grid[row][col + 1 :]
        for tree in right_view:
            right_score += 1
            if tree < num:
                continue
            else:
                break

        up_score = 0
        up_view = list(reversed(col_list[:row]))
        for tree in up_view:
            up_score += 1
            if tree < num:
                continue
            else:
                break

        down_score = 0
        down_view = col_list[row + 1 :]
        for tree in down_view:
            down_score += 1
            if tree < num:
                continue
            else:
                break
        scenic_score = left_score * right_score * up_score * down_score
        # print(num, row, col, left_score, right_score, up_score, down_score, scenic_score)
        # print(num, row, col, up_score)

        max_scenic_score = max(max_scenic_score, scenic_score)

print("PART 2 : ", max_scenic_score)

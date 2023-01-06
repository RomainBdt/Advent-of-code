# %%
# # PART 1
import pathlib
from collections import deque, defaultdict

path = pathlib.Path.cwd() / "input.txt"
data = open(path).read()

# shape1 = [(0, 2), (0, 3), (0, 4), (0, 5)]  # __
# shape2 = [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)]  # +
# shape3 = [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4)]  # _|
# shape4 = [(0, 2), (1, 2), (2, 2), (3, 2)]  # |
# shape5 = [(0, 2), (0, 3), (1, 2), (1, 3)]  # square


# def can_move_horizontally(grid, shape, dir):
#     for r, c in shape:
#         if dir == ">":
#             if c == 6:
#                 return False
#             if (r, c + 1) in grid:
#                 return False
#         else:
#             if c == 0:
#                 return False
#             if (r, c - 1) in grid:
#                 return False
#     else:
#         return True


# def move_horizontally(shape, dir):
#     new_shape = []
#     for r, c in shape:
#         if dir == ">":
#             new_shape.append((r, c + 1))
#         else:
#             new_shape.append((r, c - 1))
#     return new_shape


# def can_move_down(grid, shape):
#     for r, c in shape:
#         if (r - 1, c) in grid:
#             return False
#     else:
#         return True


# def move_down(grid, shape):
#     new_shape = []
#     for r, c in shape:
#         new_shape.append((r - 1, c))
#     return new_shape


# def init(highest_point, shape):
#     ofst = 4
#     new_shape = []
#     for r, c in shape:
#         new_shape.append((r + highest_point + ofst, c))
#     return new_shape


# def show_picture(grid, highest_point):
#     for r in reversed(range(highest_point + 1)):
#         row = []
#         for c in range(7):
#             if (r, c) in grid:
#                 row.append("#")
#             else:
#                 row.append(" ")
#         print("".join(row))


# length = len(data)
# grid = [(0, i) for i in range(7)]
# end_of_fall = True
# shapes = [shape1, shape2, shape3, shape4, shape5]
# shape_num = 0
# move_num = 0
# rocks_stopped = 0
# highest_point = 0

# # for i in range(10):
# while rocks_stopped < 10:

#     if end_of_fall:  # init an make first move
#         end_of_fall = False
#         shape = shapes[shape_num]
#         shape_num = (shape_num + 1) % len(shapes)
#         shape = move_horizontally(shape, data[move_num])
#         move_num = (move_num + 1) % len(data)
#         shape = init(highest_point, shape)
#         continue

#     if can_move_down(grid, shape):
#         # print(f'{shape} will move down')
#         shape = move_down(grid, shape)
#         # print(f'{shape} moved down')
#         move_num = (move_num + 1) % len(data)
#         if can_move_horizontally(grid, shape, data[move_num]):
#             # print(f'{shape} will move one {data[move_num]}')
#             shape = move_horizontally(shape, data[move_num])
#             # print(f'{shape} moved one {data[move_num]}')
#     else:
#         move_num = (move_num + 1) % len(data)
#         if can_move_horizontally(grid, shape, data[move_num]):
#             # print(f'{shape} will move one {data[move_num]}')
#             shape = move_horizontally(shape, data[move_num])
#             # print(f'{shape} moved one {data[move_num]}')
#         end_of_fall = True
#         grid.extend(shape)
#         rocks_stopped += 1
#         highest_point = max(highest_point, max([r for r, _ in shape]))
#         show_picture(grid, highest_point)
#         print("-" * 7)

#     # print(i, rocks_stopped, highest_point)
#     # print(grid)
#     # print('-'*10)
#     # print(shape)


# %%
# PART 1
import pathlib
from collections import deque, defaultdict

path = pathlib.Path.cwd() / "input.txt"
data = open(path).read()

MOVES = [1 if i == ">" else -1 for i in data]

SHAPES = [
    (2, 3, 4, 5),  # shape1 = [(0, 2), (0, 3), (0, 4), (0, 5)]  # __
    (
        3,
        1j + 2,
        1j + 3,
        1j + 4,
        2j + 3,
    ),  # shape2 = [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)]  # +
    (
        2,
        3,
        4,
        1j + 4,
        2j + 4,
    ),  # shape3 = [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4)]  # _|
    (2, 1j + 2, 2j + 2, 3j + 2),  # shape4 = [(0, 2), (1, 2), (2, 2), (3, 2)]  # |
    (2, 3, 1j + 2, 1j + 3),  # shape5 = [(0, 2), (0, 3), (1, 2), (1, 3)]  # square
]

n = 0
ofst = 4j
shape = [i + ofst for i in SHAPES[0]]
grid = [x for x in range(7)]
shape_num = 1
move_num = 0
rocks_stopped = 0

i = 0


def show_grid(grid):
    highest_point = max([i.imag for i in grid])

    for row in reversed(range(int(highest_point) + 1)):
        line = []
        for col in range(7):
            if complex(col, row) in grid:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))
    print("-" * 7)
    print()


while rocks_stopped < 2022:
    i += 1
    # move horizontally
    shape_temp = [i + MOVES[move_num] for i in shape]
    if (
        MOVES[move_num] == 1
        and max([z.real for z in shape_temp]) <= 6
        and all([True if s not in grid else False for s in shape_temp])
    ):
        shape = shape_temp  # Move right

    elif (
        MOVES[move_num] == -1
        and min([z.real for z in shape_temp]) >= 0
        and all([True if s not in grid else False for s in shape_temp])
    ):
        shape = shape_temp  # Move left

    move_num = (move_num + 1) % len(MOVES)

    # move down if possible
    shape_temp = [i - 1j for i in shape]
    for s in shape_temp:
        if s in grid:
            grid += shape
            rocks_stopped += 1
            highest_point = complex(0, max([i.imag for i in grid]))
            shape = [i + highest_point + ofst for i in SHAPES[shape_num]]
            shape_num = (shape_num + 1) % len(SHAPES)

            break
    else:
        shape = shape_temp

print('PART 1: ', int(highest_point.imag))


# %%
%%time
# PART 2
import pathlib
from itertools import dropwhile
import time

path = pathlib.Path.cwd() / "input.txt"
data = open(path).read()

MOVES = [1 if i == ">" else -1 for i in data]

SHAPES = [
    (2, 3, 4, 5),  # shape1 = [(0, 2), (0, 3), (0, 4), (0, 5)]  # __
    (
        3,
        1j + 2,
        1j + 3,
        1j + 4,
        2j + 3,
    ),  # shape2 = [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)]  # +
    (
        2,
        3,
        4,
        1j + 4,
        2j + 4,
    ),  # shape3 = [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4)]  # _|
    (2, 1j + 2, 2j + 2, 3j + 2),  # shape4 = [(0, 2), (1, 2), (2, 2), (3, 2)]  # |
    (2, 3, 1j + 2, 1j + 3),  # shape5 = [(0, 2), (0, 3), (1, 2), (1, 3)]  # square
]

n = 0
ofst = 4j
shape = [i + ofst for i in SHAPES[0]]
grid = {x for x in range(7)}
shape_num = 1
move_num = 0
rocks_stopped = 0

i = 0


def show_grid(grid):
    highest_point = max([i.imag for i in grid])

    for row in reversed(range(int(highest_point) + 1)):
        line = []
        for col in range(7):
            if complex(col, row) in grid:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))
    print("-" * 7)
    print()

seen = {}
t_start = time.time()

def top_view():
    top_row = [-20] * 7
    for x in grid:
        r = int(x.imag)
        c = int(x.real)
        top_row[c] = max(top_row[c], r)
    scale = min(top_row)
    return tuple(x - scale for x in top_row)
        

cycles = 1000000000000
while rocks_stopped < cycles:

    i += 1
    
    # move horizontally
    shape_temp = {x + MOVES[move_num] for x in shape}
    if (all([0 <= z.real <= 6 for z in shape_temp]) and not (shape_temp & grid)):
        shape = shape_temp  # Move right

    move_num = (move_num + 1) % len(MOVES)

    # move down if possible
    shape_temp = {i - 1j for i in shape}
    for s in shape_temp:
        if s in grid:
            grid = grid | shape
            rocks_stopped += 1
            highest_point = complex(0, max([i.imag for i in grid]))
            shape = {i + highest_point + ofst for i in SHAPES[shape_num]}
            shape_num = (shape_num + 1) % len(SHAPES)
            
            key = (move_num, shape_num, top_view())
            if key in seen:
                rocks_stopped_prev, highest_point_prev = seen[key]
                remaining = cycles - rocks_stopped    
                rep = remaining // (rocks_stopped - rocks_stopped_prev)
                rocks_stopped += (rocks_stopped - rocks_stopped_prev) * rep
                offset = (highest_point - highest_point_prev) * rep
                seen = {}
                print('already seen', key, rep, highest_point)
            else:
                seen[key] = (rocks_stopped, highest_point)
            break
    else:
        shape = shape_temp
    if i % 1000000 == 0:
        print(i, rocks_stopped, time.time() - t_start, (1000000000000 / rocks_stopped / 3600) * (time.time() - t_start))


print('PART 2:', int(highest_point.imag + offset.imag))

# %%

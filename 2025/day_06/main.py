from pathlib import Path
from time import time


start_time = time()
file_num = 2
filename = "test.txt" if file_num == 1 else "input.txt"
path = Path(__file__).resolve().parent / filename

with open(path, mode="r", encoding="utf-8") as fid:
    puzzle = [line.strip().split() for line in fid]

grand_total = 0
cols = len(puzzle[0])

for i in range(cols):
    operator = puzzle[-1][i]
    numbers = [int(x[i]) for x in puzzle[:-1]]
    if operator == "*":
        result = 1
        for number in numbers:
            result *= number
    else:
        result = sum(numbers)
    grand_total += result
       
print("Part 1:", grand_total)

with open(path, mode="r", encoding="utf-8") as fid:
    puzzle = [line for line in fid]
operators = puzzle[-1].split()
cols = len(puzzle[0])

numbers = []
results = []
for i in range(cols):
    numbers.append(("".join([x[i] for x in puzzle[:-1]])).strip())
    if numbers[-1] == '':
        operator = operators.pop(0)
        if operator == "*":
            temp = 1
            for num in numbers[:-1]:
                temp *= int(num)
        else:
            temp = sum([int(x) for x in numbers[:-1]])
        results.append(temp)
        numbers = []


print("Part 2:", sum(results))

print(f"Time: {time() - start_time:.6f} seconds")
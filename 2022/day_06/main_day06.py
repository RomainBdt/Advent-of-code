# %%
import pathlib

path = pathlib.Path.cwd() / "input.txt"
S = open(path).read()

# %% Part 1
n = 4
for i, s in enumerate(S[:-n]):
    if len(set(S[i : i + n])) == n:
        print(i + n)
        break

# %% Part 2
n = 14
for i, s in enumerate(S[:-n]):
    if len(set(S[i : i + n])) == n:
        print(i + n)
        break

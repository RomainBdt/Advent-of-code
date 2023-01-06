# %%
import pathlib


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)


class folder:
    def __init__(self, line, parent):
        self.dir_name = line.split()[1]
        self.content = {}
        self.size = 0
        self.parent = parent

    def add_content(self, line):
        if line.startswith("dir"):
            self.content[line.split()[1]] = folder(line, parent=self)
        else:
            self.content[line.split()[1]] = file(line)

    def __iadd__(self, other):
        return self.size + other

    def update_folder_size(self):
        folder_size = 0
        for item in self.content.keys():
            if isinstance(self.content[item], folder):
                self.content[item].update_folder_size()
            folder_size += self.content[item].size

        self.size = folder_size

        if folder_size < 100000:
            global total_small_file_size
            total_small_file_size += self.size

    def find_best_folder_size(self):
        global best_folder_size
        global main_folder_size
        for item in self.content.keys():
            if isinstance(self.content[item], folder):
                self.content[item].find_best_folder_size()
            if (main_folder_size - self.size) < 40000000:
                best_folder_size = min(best_folder_size, self.size)


class file:
    def __init__(self, line) -> None:
        self.name = line.split()[1]
        self.size = int(line.split()[0])

    def __add__(self, other):
        return self.size + other


filesystem = folder(r"dir main", parent=None)
current_dir = filesystem
total_small_file_size = 0
best_folder_size = float("inf")
for line in data[1:]:
    if line.startswith("$ ls"):
        continue
    elif line.startswith("$ cd .."):
        current_dir = current_dir.parent
    elif line.startswith("$ cd"):
        new_dir = line.split()[2]
        current_dir = current_dir.content[new_dir]
    else:
        current_dir.add_content(line)


filesystem.update_folder_size()
main_folder_size = filesystem.size
filesystem.find_best_folder_size()
print("PART 1", total_small_file_size)
print("PART 2", best_folder_size)
# %%

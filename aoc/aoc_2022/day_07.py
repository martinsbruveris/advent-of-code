def parse_output(lines, idx):
    tree = dict()
    while idx < len(lines):
        if lines[idx] == "$ ls":
            idx += 1
            while idx < len(lines) and lines[idx][0] != "$":
                size, name = lines[idx].split(" ")  # "122 file_name" or "dir dir_name"
                tree[name] = dict() if size == "dir" else int(size)
                idx += 1
        elif lines[idx] == "$ cd ..":
            idx += 1
            break
        else:
            _, _, name = lines[idx].split(" ")  # $ cd dir_name
            tree[name], idx = parse_output(lines, idx + 1)
    return tree, idx


def dir_sizes(tree):
    sizes = []
    curr_size = 0
    for name, value in tree.items():
        if isinstance(value, dict):
            sub_sizes = dir_sizes(value)
            curr_size += sub_sizes[0]
            sizes.extend(sub_sizes)
        else:
            curr_size += value
    # We always return the size of the current directory at index 0
    return [curr_size] + sizes


def main(data, part):
    lines = data.split("\n")
    tree, _ = parse_output(lines, 1)
    sizes = dir_sizes(tree)

    if part == "a":
        result = sum(filter(lambda s: s <= 100_000, sizes))
    else:
        need_to_free = sizes[0] - 40_000_000  # Index 0 holds the root size
        result = min(filter(lambda s: s >= need_to_free, sizes))
    return result

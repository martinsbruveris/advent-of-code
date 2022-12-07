def main(data, part):
    n = 4 if part == "a" else 14
    for j in range(n, len(data)):
        if len(set(data[j - n : j])) == n:
            return j

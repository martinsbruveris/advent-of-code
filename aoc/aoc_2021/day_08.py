def parse_line(line):
    patterns, output = line.split(" | ")
    patterns = ["".join(sorted(s)) for s in patterns.split(" ")]
    output = ["".join(sorted(s)) for s in output.split(" ")]
    return patterns, output


def count_1478(lines):
    count = 0
    for line in lines:
        _, output = parse_line(line)
        count += sum(len(s) in {2, 3, 4, 7} for s in output)
    return count


def decode_pattern(pattern):
    code = {
        1: next(s for s in pattern if len(s) == 2),
        4: next(s for s in pattern if len(s) == 4),
        7: next(s for s in pattern if len(s) == 3),
        8: next(s for s in pattern if len(s) == 7),
    }
    zero_six_nine = {s for s in pattern if len(s) == 6}
    # 9 is the only one of {0, 6, 9} that contains 4
    code[9] = next(s for s in zero_six_nine if set(code[4]).issubset(set(s)))
    zero_six = zero_six_nine - {code[9]}
    # 0 is the only one of {0, 6} that contains 7
    code[0] = next(s for s in zero_six if set(code[7]).issubset(set(s)))
    # 6 is the remaining one
    code[6] = (zero_six - {code[0]}).pop()

    two_three_five = {s for s in pattern if len(s) == 5}
    # 3 is the only one of {2, 3, 5} that contains 7
    code[3] = next(s for s in two_three_five if set(code[7]).issubset(set(s)))
    two_five = two_three_five - {code[3]}
    # 5 is the only one of {2, 5} that is contained in 9
    code[5] = next(s for s in two_five if set(s).issubset(set(code[9])))
    # 2 is the remaining one
    code[2] = (two_five - {code[5]}).pop()

    # Reverse code
    decoder = {v: k for k, v in code.items()}
    return decoder


def decode_output(line):
    pattern, output = parse_line(line)
    decoder = decode_pattern(pattern)
    output = [decoder[s] for s in output]
    result = 0
    for d in output:
        result = 10 * result + d
    return result


def main(data, part):
    lines = data.split("\n")

    if part == "a":
        result = count_1478(lines)
    else:
        outputs = [decode_output(line) for line in lines]
        result = sum(outputs)
    return result

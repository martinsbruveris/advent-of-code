a_op = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6}
b_op = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}


def main(data, part):
    lines = data.split("\n")
    op = a_op if part == "a" else b_op
    result = sum(map(lambda c: op[c.replace(" ", "")], lines))
    return result

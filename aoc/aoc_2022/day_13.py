from functools import partial


def parse(s: str, ind: int = 0):
    return_index = ind != 0
    result = []
    ind += 1  # First character is "["
    while s[ind] != "]":
        if s[ind] == ",":
            ind += 1
        elif s[ind] == "[":
            sub_result, ind = parse(s, ind)
            result.append(sub_result)
        else:  # Parse a number
            end = ind
            while s[end] in "0123456789":
                end += 1
            sub_packet = s[ind:end]
            result.append(int(sub_packet))
            ind += len(sub_packet)
    ind += 1
    return result, ind if return_index else result


def leq(pair_1, pair_2):
    return compare(pair_1, pair_2) in {0, 1}


def compare(pair_1, pair_2):
    for a, b in zip(pair_1, pair_2):
        if isinstance(a, int) and isinstance(b, int):
            res = 1 if a < b else (-1 if a > b else 0)
        elif isinstance(a, int) and isinstance(b, list):
            res = compare([a], b)
        elif isinstance(a, list) and isinstance(b, int):
            res = compare(a, [b])
        else:
            res = compare(a, b)
        if res != 0:
            return res
    if len(pair_1) < len(pair_2):
        return 1
    elif len(pair_1) > len(pair_2):
        return -1
    else:
        return 0


def main(data, part):
    if part == "a":
        pairs = data.split("\n\n")
        result = sum(
            j * leq(*map(parse, pair.split("\n"))) for j, pair in enumerate(pairs, 1)
        )
    else:
        packets = data.replace("\n\n", "\n").split("\n")
        packets = list(map(parse, packets))
        split_1 = sum(map(partial(leq, pair_2=[[2]]), packets))
        split_2 = sum(map(partial(leq, pair_2=[[6]]), packets))
        result = (split_1 + 1) * (split_2 + 2)
    return result

from math import prod

operator_map = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda v: int(v[0] > v[1]),
    6: lambda v: int(v[0] < v[1]),
    7: lambda v: int(v[0] == v[1]),
}


def parse_packet(bits, idx):
    versions = [int(bits[idx : idx + 3], 2)]
    type_id = int(bits[idx + 3 : idx + 6], 2)
    idx += 6
    if type_id == 4:  # Parse literal
        number = ""
        while bits[idx] == "1":
            number += bits[idx + 1 : idx + 5]
            idx += 5
        number += bits[idx + 1 : idx + 5]  # Last block starting with 0
        idx += 5
        value = int(number, 2)
    else:  # Parse operator
        length_id = bits[idx]
        idx += 1
        sub_values = []
        if length_id == "0":  # We are given length in bits
            num_bits = int(bits[idx : idx + 15], 2)
            idx += 15
            sub_end = idx + num_bits
            while idx < sub_end:
                sub_versions, sub_value, idx = parse_packet(bits, idx)
                versions.extend(sub_versions)
                sub_values.append(sub_value)
        else:  # We are given number of sub-packets
            num_packets = int(bits[idx : idx + 11], 2)
            idx += 11
            for _ in range(num_packets):
                sub_versions, sub_value, idx = parse_packet(bits, idx)
                versions.extend(sub_versions)
                sub_values.append(sub_value)
        value = operator_map[type_id](sub_values)

    return versions, value, idx


def main(data, part):
    bits = "".join(f"{int(c, 16):04b}" for c in data)
    versions, value, _ = parse_packet(bits, 0)
    return sum(versions) if part == "a" else value

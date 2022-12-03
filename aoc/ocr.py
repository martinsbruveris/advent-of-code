"""
Adapted from: https://github.com/wimglenn/advent-of-code-wim/blob/main/aoc_wim/ocr.py
"""
import numpy as np

glyphs = """
.##.
#..#
#..#
####
#..#
#..#


..##..
.#..#.
#....#
#....#
#....#
######
#....#
#....#
#....#
#....#


###.
#..#
###.
#..#
#..#
###.


#####.
#....#
#....#
#....#
#####.
#....#
#....#
#....#
#....#
#####.


.##.
#..#
#...
#...
#..#
.##.


.####.
#....#
#.....
#.....
#.....
#.....
#.....
#.....
#....#
.####.


####
#...
###.
#...
#...
####


######
#.....
#.....
#.....
#####.
#.....
#.....
#.....
#.....
######


####
#...
###.
#...
#...
#...


######
#.....
#.....
#.....
#####.
#.....
#.....
#.....
#.....
#.....


.##.
#..#
#...
#.##
#..#
.###


.####.
#....#
#.....
#.....
#.....
#..###
#....#
#....#
#...##
.###.#


#..#
#..#
####
#..#
#..#
#..#


#....#
#....#
#....#
#....#
######
#....#
#....#
#....#
#....#
#....#


#...#
#...#
#...#
#####
#...#
#...#
#...#
#...#


###
.#.
.#.
.#.
.#.
###


###
.#.
.#.
.#.
.#.
.#.
.#.
###


..##
...#
...#
...#
#..#
.##.


...###
....#.
....#.
....#.
....#.
....#.
....#.
#...#.
#...#.
.###..


#....#
#...#.
#..#..
#.#...
##....
##....
#.#...
#..#..
#...#.
#....#


#..#
#.#.
##..
#.#.
#.#.
#..#


#...
#...
#...
#...
#...
####


#.....
#.....
#.....
#.....
#.....
#.....
#.....
#.....
#.....
######


#....#
##...#
##...#
#.#..#
#.#..#
#..#.#
#..#.#
#...##
#...##
#....#


.##.
#..#
#..#
#..#
#..#
.##.


###.
#..#
#..#
###.
#...
#...


#####.
#....#
#....#
#....#
#####.
#.....
#.....
#.....
#.....
#.....


###.
#..#
#..#
###.
#.#.
#..#


#####.
#....#
#....#
#....#
#####.
#..#..
#...#.
#...#.
#....#
#....#


.###
#...
#...
.##.
...#
###.


#..#
#..#
#..#
#..#
#..#
.##.


#....#
#....#
.#..#.
.#..#.
..##..
..##..
.#..#.
.#..#.
#....#
#....#


####
...#
..#.
.#..
#...
####


######
.....#
.....#
....#.
...#..
..#...
.#....
#.....
#.....
######


#####
#...#
#...#
#...#
#####
"""


def str2arr(s):
    arr = [list(line) for line in s.split("\n")]
    arr = np.asarray(arr)
    arr = (arr == "#").astype(int)
    return arr


def autocrop(arr):
    on = np.argwhere(arr)
    if not on.size:
        return arr[:0, :0]
    r0, c0 = on.min(axis=0)
    r1, c1 = on.max(axis=0) + 1
    return arr[r0:r1, c0:c1]


glyphs = {g: str2arr(g) for g in glyphs.strip().split("\n\n\n")}
known = dict(zip(glyphs, "AABBCCEEFFGGHHHIIJJKKLLNOPPRRSUXZZ□"))
known[""] = ""


def aocr(item: np.ndarray) -> str:
    item = autocrop(item)
    if item.size == 0:
        return ""

    txt = "\n".join(["".join(map(str, line)) for line in item])
    txt = txt.replace("1", "#").replace("0", ".")

    h_total = item.shape[0]
    for k, v in glyphs.items():
        h, w = v.shape
        if h == h_total and (item[:, :w] == v).all():
            letter = known[k]
            return letter + aocr(item[:, w:])

    print("AOCR does not understand this item:")
    print(txt)
    print("Identify it and add to {}".format(__file__))
    raise ValueError(txt)

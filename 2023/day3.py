#!/usr/bin/env python3

import re
from typing import List, Optional, Dict

def isAdj(symbolIndexes: List[List[int]], lineIdx: int, numIdx: int, num: int) -> bool:
    adjLinesIndexes = []
    for i in [lineIdx + i for i in range(-1,2) if lineIdx + i >= 0 and lineIdx + i < len(symbolIndexes)]:
        adjLinesIndexes.extend(symbolIndexes[i])
    return any((index in range(numIdx-1, numIdx+len(str(num))+1)) for index in adjLinesIndexes)

def adjNums(lineIdx: int, gearIdx: int, numPositions: List[Dict[int, int]]) -> Optional[List[int]]:
    adjLines = [numPositions[i] for i in range(max(0, lineIdx-1), min(len(numPositions), lineIdx+2))]
    return [num for line in adjLines for idx, num in line.items() if gearIdx in range(idx-1, idx+len(str(num))+1)]

def part2() -> int:
    with open("inputs/day3.txt", "r") as f:
        # TODO oder alle anderen Zeichen herauslöschen
        powers = []
        lines = f.read().splitlines()
        gearIdxs = [[i for i, c in enumerate(l) if c == "*"] for l in lines]
        numPositions = [{ m.start(): int(m.group()) for m in re.finditer(r"\d+", l)} for l in lines]
        for lineIdx, idxs in enumerate(gearIdxs):
            for gearIdx in idxs:
                nums = adjNums(lineIdx, gearIdx, numPositions)
                if len(nums) >= 2:
                    powers.append(nums[0] * nums[1])
        return sum(powers)

def part1() -> int:
    with open("inputs/day3.txt", "r") as f:
        lines = f.read().splitlines()
        sIdxs = [[i for i, c in enumerate(l) if not c.isdigit() and c != "."] for l in lines]
        validNums = [int(m.group()) for lIdx, l in enumerate(lines) for m in re.finditer(r"\d+", l) if isAdj(sIdxs, lIdx, m.start(), int(m.group()))]
        return sum(validNums)

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
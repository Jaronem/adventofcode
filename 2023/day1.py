#!/usr/bin/env python3

import re

def part1():
    with open("inputs/day1.txt", "r") as f:
        lines = f.readlines()
        calValues = []
        for l in lines:
            digits = [int(c) for c in l if c.isdigit()]
            calValues.append(digits[0]*10 + digits[len(digits)-1])
        return sum(calValues)

numberDict = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }

def part2(): 
    with open("inputs/day1.txt", "r") as f:
        lines = f.readlines()
        calValues = []
        for l in lines:
            idxValues = {}
            for i, c in enumerate(l):
                if c.isdigit():
                    idxValues[i] = int(c)
            for k, v in numberDict.items():
                for oc in[m.start() for m in re.finditer(k, l)]:
                    idxValues[oc] = v
            indexes = sorted(idxValues)
            calValues.append(idxValues[indexes[0]] * 10 + idxValues[indexes[len(indexes) - 1]])
        return sum(calValues)
    
if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
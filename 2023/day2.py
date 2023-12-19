#!/usr/bin/env python3

import re
from functools import reduce

maxDict = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

def part2() -> int:
    powers = []
    with open("inputs/day2.txt", "r") as f:
        for l in f.read().splitlines():
            parts = l.split(":")
            maxes = {}
            for gameSet in parts[1].split(";"):
                colorCombinations = [[int(re.findall(r"\d+", c.strip())[0]), re.sub(r"\d+", "", c).strip()] for c in gameSet.split(", ")]
                for amnt, color in colorCombinations: 
                    if not color in maxes or maxes[color] < amnt:
                        maxes[color] = amnt
            powers.append(reduce(lambda x, y: x*y, maxes.values()))
    return sum(powers)

def part1() -> int:
    gameIds = []
    with open("inputs/day2.txt", "r") as f:
        for l in f.read().splitlines():
            parts = l.split(":")
            gameId = int(parts[0][len("Game "):])
            gamePossible = True
            for gameSet in parts[1].split(";"):
                colorCombinations = [[int(re.findall(r"\d+", c.strip())[0]), re.sub(r"\d+", "", c).strip()] for c in gameSet.split(", ")]
                if not all(maxDict[color] >= amnt for amnt, color in colorCombinations):
                    gamePossible = False
                    break
            if gamePossible: gameIds.append(gameId)
    return sum(gameIds)

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
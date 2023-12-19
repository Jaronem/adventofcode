#!/usr/bin/env python3

from typing import List, Tuple
from collections import defaultdict

def parseNumbers(line: str) -> Tuple[List[int],List[int]]:
    return [[int(n) for n in nums.split()] for nums in line.split(":")[1].split("|")]

def winnings(lines: List[str]) -> List[int]:
    return [len(set(winningNums) & set(myNums)) for winningNums, myNums in map(parseNumbers, lines)]

def part1():
    with open("inputs/day4.txt", "r") as f:
        return sum([2 ** (wins - 1) if wins > 1 else wins for wins in winnings(f.read().splitlines())])

def part2():
    copies = defaultdict(lambda: 0)
    with open("inputs/day4.txt", "r") as f:
        cardWins = winnings(f.read().splitlines())
        def calcNextCards(cardId: int):
            winCount = cardWins[cardId]
            for nextCard in range(cardId+1, min(cardId+winCount+1, len(cardWins))):
                copies[nextCard] += 1
                calcNextCards(nextCard)

        for cardId in range(0, len(cardWins)):
            copies[cardId] += 1
            calcNextCards(cardId)
    return sum(copies.values())

        

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
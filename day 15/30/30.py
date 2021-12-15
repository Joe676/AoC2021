import os
from queue import PriorityQueue
from dataclasses import dataclass, field
from math import sqrt, inf

def on_board(p:tuple[int, int], dim:int)-> bool: 
    """Checks whether the position is on a square board of certain dimension."""
    return p[0] >= 0 and p[1] >= 0 and p[0] < dim and p[1] < dim

def cost(r:list[tuple[int, int]], lines:list[str]) -> int:
    """Calculates cost of traveling the given road in a given board"""
    out = 0
    for x, y in r:
        out += int(lines[x][y])
    return out

def distance(p:tuple[int, int], goal:tuple[int, int]) -> int:
    dx = p[0]-goal[0]
    dy = p[1]-goal[1]
    return int(sqrt(dx*dx + dy*dy))

def main2():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "30_input.txt")
    f = open(filename, 'r')
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

    n = len(lines)
    N = n*5
    cave = []
    for i in range(N):
        cave.append([])
        for j in range(N):
            a = (int(lines[i%n][j%n]) + i//n + j//n)
            cave[i].append( a-9 if a>=10 else a )

    costs = [[inf for __ in range(N)] for _ in range(N)]
    parent = [[None for __ in range(N)] for _ in range(N)]
    pq = PriorityQueue()
    pq.put((0, (0, 0))) #Starting node
    while not pq.empty():
        d, pos = pq.get()
        print(d, pos)
        if pos == (N-1, N-1):
            return d
        for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            p = (pos[0]+x, pos[1]+y)
            if on_board(p, N) and costs[p[0]][p[1]] > d + int(cave[p[0]][p[1]]):
                costs[p[0]][p[1]] = d + int(cave[p[0]][p[1]])
                parent[p[0]][p[1]] = pos
                pq.put((costs[p[0]][p[1]], p))
    


if __name__ == "__main__":
    print(main2())
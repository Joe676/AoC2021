import os
from queue import PriorityQueue
from dataclasses import dataclass, field
from math import sqrt, inf
# from typing import Tuple, List

@dataclass(order=True)
class PrioritizedItem:
    distance: int
    position: tuple[int, int]=field(compare=False)
    route: list[tuple[int, int]]=field(compare=False)

#A*
def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "29_input.txt")
    f = open(filename, 'r')
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

    N = len(lines)
    # vis = [[False for __ in range(N)] for _ in range(N)]
    
    pq = PriorityQueue()
    pq.put(PrioritizedItem(0, (0, 0), [])) #Starting node
    goal = (N-1, N-1)
    while not pq.empty():
        item:PrioritizedItem = pq.get()
        if item.position == goal:
            return cost(item.route, lines)
        for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            p = (item.position[0]+x, item.position[1]+y)
            r = item.route.copy()
            if on_board(p, N) and not p in r:
                print(r)
                r.append(p)
                d = cost(r, lines) + distance(p, goal)
                pq.put(PrioritizedItem(d, p, r))

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
    filename = os.path.join(dirname, "29_input.txt")
    f = open(filename, 'r')
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

    N = len(lines)
    costs = [[inf for __ in range(N)] for _ in range(N)]
    parent = [[None for __ in range(N)] for _ in range(N)]
    pq = PriorityQueue()
    pq.put((0, (0, 0))) #Starting node
    while not pq.empty():
        d, pos = pq.get()
        print(d, pos)
        if pos == (N-1, N-1):
            for l in costs:
                print(l)
            return d
        for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            p = (pos[0]+x, pos[1]+y)
            if on_board(p, N) and costs[p[0]][p[1]] > d + int(lines[p[0]][p[1]]):
                costs[p[0]][p[1]] = d + int(lines[p[0]][p[1]])
                parent[p[0]][p[1]] = pos
                pq.put((costs[p[0]][p[1]], p))
    


if __name__ == "__main__":
    print(main2())
import sys

INPUT = "1,1,3,5,1,3,2,1,5,3,1,4,4,4,1,1,1,3,1,4,3,1,2,2,2,4,1,1,5,5,4,3,1,1,1,1,1,1,3,4,1,2,2,5,1,3,5,1,3,2,5,2,2,4,1,1,1,4,3,3,3,1,1,1,1,3,1,3,3,4,4,1,1,5,4,2,2,5,4,5,2,5,1,4,2,1,5,5,5,4,3,1,1,4,1,1,3,1,3,4,1,1,2,4,2,1,1,2,3,1,1,1,4,1,3,5,5,5,5,1,2,2,1,3,1,2,5,1,4,4,5,5,4,1,1,3,3,1,5,1,1,4,1,3,3,2,4,2,4,1,5,5,1,2,5,1,5,4,3,1,1,1,5,4,1,1,4,1,2,3,1,3,5,1,1,1,2,4,5,5,5,4,1,4,1,4,1,1,1,1,1,5,2,1,1,1,1,2,3,1,4,5,5,2,4,1,5,1,3,1,4,1,1,1,4,2,3,2,3,1,5,2,1,1,4,2,1,1,5,1,4,1,1,5,5,4,3,5,1,4,3,4,4,5,1,1,1,2,1,1,2,1,1,3,2,4,5,3,5,1,2,2,2,5,1,2,5,3,5,1,1,4,5,2,1,4,1,5,2,1,1,2,5,4,1,3,5,3,1,1,3,1,4,4,2,2,4,3,1,1"

"""
Solution for day 6 puzzles of Advent of Code 2021

In this program the fish aren't simulated themselves - instead there is a counter remembering how many fish there are at each clock cycle.
"""

def main():
    fish_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    start_fish = [int(x) for x in INPUT.rstrip().split(',')]
    for x in start_fish:
        fish_counter[x]+=1
    
    N_DAYS = 80 #256 for puzzle #2
    for i in range(N_DAYS):
        to_be_born = fish_counter[0]
        now = fish_counter[8]
        save = 0
        for i in range(8, 0, -1):
            save = fish_counter[i-1]
            fish_counter[i-1] = now
            now = save
        fish_counter[6] += to_be_born
        fish_counter[8] = to_be_born
    return sum(fish_counter)

if __name__ == "__main__":
    print(main())
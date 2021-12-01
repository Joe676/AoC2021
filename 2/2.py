"""
Solution for exercise 2 of Advent of Code 2021

In order to find the number of times the depth gets bigger
in windows of width 3, it goes over all the values of i from
0 to N-3 and compares the sums of sub lists using built-in 
python capabilities of list indexing
"""

def main():
    f = open("2/2_input.txt", "r")
    lines = f.readlines()
    f.close()
    lines = [int(x) for x in lines]
    count = 0
    for i in range(len(lines)-3):
        count += 1 if sum(lines[i:i+3]) < sum(lines[i+1:i+4]) else 0 #lines[i:i+3] creates a sublist of width 3 starting at index i
    print(count)

if __name__ == "__main__":
    main()
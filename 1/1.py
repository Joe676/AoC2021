"""
Solution for exercise 1 of Advent of Code 2021

In order to find the number of times the depth gets bigger
it iterates over all the measurements and compares each one
to the previous one - incrementing count each time we go deeper.
"""

def main():
    f = open("1_input.txt", "r")
    count = 0
    lines = f.readlines()
    f.close()
    prev = int(lines[0])
    for line in lines[1:]:
        cur = int(line)
        if cur > prev:
            count += 1
        prev = cur
    print(count)

if __name__ == "__main__":
    main()
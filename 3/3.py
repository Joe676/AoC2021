"""
Solution for exercise 3 of Advent of Code 2021

Each line of input is parsed and then variables x and y are updated accordingly.
"""

def main():
    f = open("3/3_input.txt", "r")
    lines = f.readlines()
    f.close()
    x = 0
    y = 0

    for line in lines:
        line.rstrip()
        l = line.split(" ")
        opt = l[0]
        h = int(l[1])
        if opt == "forward":
            x+=h
        elif opt == "down":
            y+=h
        elif opt == "up":
            y-=h
    return (x, y)


if __name__ == "__main__":
    x, y = main()
    print(x, y, x*y)
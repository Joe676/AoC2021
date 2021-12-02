"""
Solution for exercise 3 of Advent of Code 2021

Each line of input is parsed and then variables x, y and aim are updated accordingly.
"""

def main():
    f = open("4/4_input.txt", "r")
    lines = f.readlines()
    f.close()

    aim = 0
    x, y = 0, 0

    for line in lines:
        line.rstrip()
        l = line.split(" ")
        opt = l[0]
        h = int(l[1])
        if opt == "forward":
            x+=h
            y+=h*aim
        elif opt == "down":
            aim+=h
        elif opt == "up":
            aim-=h
    return (x, y)

if __name__ == "__main__":
    x, y = main()
    print(x, y, x*y)
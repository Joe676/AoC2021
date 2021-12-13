import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "26_input.txt")
    f = open(filename, 'r')
    lines = [l.rstrip() for l in f.readlines()]
    f.close()
    
    dots = []
    folds = []

    for line in lines:
        if len(line)>0 and line[0].isnumeric():
            dots.append(tuple(int(x) for x in line.split(',')))
        elif len(line)>0 and line[0] == 'f':
            fold = line.split(' ')[-1]
            folds.append((fold.split('=')[0], int(fold.split('=')[1])))
    for axis, val in folds:
        if axis == 'y':
            for i in range(len(dots)-1, -1, -1):
                dot = dots[i]
                newDot = None
                if dot[1] > val:
                    newDot = (dot[0], val - abs(val-dot[1]))
                    dots.remove(dot)
                if newDot and newDot not in dots:
                    dots.append(newDot)
        elif axis == 'x':
            for i in range(len(dots)-1, -1, -1):
                dot = dots[i]
                newDot = None
                if dot[0] > val:
                    newDot = (val - abs(val-dot[0]), dot[1])
                    dots.remove(dot)
                if newDot and newDot not in dots:
                    dots.append(newDot)
    
    dims = [0, 0]
    for dot in dots:
        for i in (0, 1):
            if dot[i] > dims[i]:
                dims[i] = dot[i]
    board = [[' ' for __ in range(dims[0]+1)] for _ in range(dims[1]+1)]

    for dot in dots:
        board[dot[1]][dot[0]] = '#'

    for l in board:
        print(*l)


if __name__ == "__main__":
    main()
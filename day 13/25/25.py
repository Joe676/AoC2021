import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "25_input.txt")
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
    axis, val = folds[0]
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
    
    print(len(dots))
                


if __name__ == "__main__":
    main()
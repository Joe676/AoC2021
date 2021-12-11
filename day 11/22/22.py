import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "22_input.txt")
    f = open(filename, 'r')
    lines = [l.rstrip() for l in f.readlines()]
    f.close()
    lines = [[int(l) for l in line] for line in lines]
    flashed = [[False for _ in line] for line in lines]
    step = 0
    while(True):
        step += 1
        print(step)
        for i, line in enumerate(lines):
            for j, l in enumerate(line):
                lines[i][j] += 1
        
        for i, line in enumerate(lines):
            for j, l in enumerate(line):
                if l > 9:#FLASH
                    flashed[i][j] = True
                    for i_off in range(-1, 2):
                        for j_off in range(-1, 2):
                            if on_board(i+i_off, j+j_off, len(lines), len(line)):
                                lines[i+i_off][j+j_off] += 1
                    if flashed[i][j]:
                        lines[i][j] = 0


        while any([any([l>9 for l in line]) for line in lines]):
            for i, line in enumerate(lines):
                for j, l in enumerate(line):
                    if l > 9 and not flashed[i][j]:#FLASH
                        flashed[i][j] = True
                        for i_off in range(-1, 2):
                            for j_off in range(-1, 2):
                                if on_board(i+i_off, j+j_off, len(lines), len(line)):
                                    lines[i+i_off][j+j_off] += 1
                    if flashed[i][j]:
                        lines[i][j] = 0

                
        if all([all([f for f in f_line]) for f_line in flashed]):
            for i in range(len(flashed)):
                print(flashed[i])
            return step
        for i in range(len(flashed)):
            for j in range(len(flashed[i])):
                if flashed[i][j]:
                    lines[i][j] = 0
                flashed[i][j] = False


def on_board(x, y, max_x, max_y):
    return x >= 0 and x < max_x and y >= 0 and y < max_y

if __name__ == "__main__":
    print(main())
import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "21_input.txt")
    f = open(filename, 'r')
    lines = [l.rstrip() for l in f.readlines()]
    f.close()
    lines = [[int(l) for l in line] for line in lines]
    flashed = [[False for _ in line] for line in lines]

    steps_num = 100
    flashes_count = 0
    for _ in range(steps_num):
        for i, line in enumerate(lines):
            for j, l in enumerate(line):
                lines[i][j] += 1
        
        for i, line in enumerate(lines):
            # print(line)
            for j, l in enumerate(line):
                if l > 9:#FLASH
                    flashes_count += 1
                    flashed[i][j] = True
                    for i_off in range(-1, 2):
                        for j_off in range(-1, 2):
                            if on_board(i+i_off, j+j_off, len(lines), len(line)):
                                lines[i+i_off][j+j_off] += 1
                    if flashed[i][j]:
                        lines[i][j] = 0
        # print()
        while any([any([l>9 for l in line]) for line in lines]):
            # print('a')
            for i, line in enumerate(lines):
                # print(line)
                for j, l in enumerate(line):
                    # print(l, flashed[i][j])
                    if l > 9 and not flashed[i][j]:#FLASH
                        # print(l, "FLASH")
                        flashes_count += 1
                        flashed[i][j] = True
                        for i_off in range(-1, 2):
                            for j_off in range(-1, 2):
                                if on_board(i+i_off, j+j_off, len(lines), len(line)):
                                    lines[i+i_off][j+j_off] += 1
                    if flashed[i][j]:
                        lines[i][j] = 0
            # print()
        for i in range(len(flashed)):
            for j in range(len(flashed[i])):
                if flashed[i][j]:
                    lines[i][j] = 0
                flashed[i][j] = False
            # print(lines[i])
        # print(_, ": ", flashes_count)
    print(flashes_count)


def on_board(x, y, max_x, max_y):
    return x >= 0 and x < max_x and y >= 0 and y < max_y

if __name__ == "__main__":
    main()
import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "18_input.txt")
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    lines = [line.rstrip() for line in lines]
    vis = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]

    is_lowpoint = True
    basins = []
    for i, line in enumerate(lines):
        for j, height in enumerate(line):
            height = int(height)
            basin_size = 0
            
            for i_off, j_off in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if i_off == 0 and j_off == 0:
                    continue
                if on_board(i+i_off, j+j_off, len(lines), len(line)):
                    if int(lines[i+i_off][j+j_off]) < height:
                        is_lowpoint = False
                        break
            if is_lowpoint:
                vis[i][j] = True
                basin_size += 1
                basin_size += find_basin(i, j, lines, vis)
            is_lowpoint = True
            basins.append(basin_size)
    out = 1
    for _ in range(3):
        out *= max(basins)
        basins.remove(max(basins))
    print(out)



def find_basin(x, y, lines, vis):
    out = 0
    for x_off, y_off in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if x_off == 0 and y_off == 0:
            continue
        if on_board(x+x_off, y+y_off, len(lines), len(lines[0])) and not vis[x+x_off][y+y_off] and int(lines[x+x_off][y+y_off]) != 9:
            vis[x+x_off][y+y_off] = True
            out += 1 + find_basin(x+x_off, y+y_off, lines, vis)
    return out
                            

def on_board(x, y, max_x, max_y):
    return x >= 0 and x < max_x and y >= 0 and y < max_y

if __name__ == "__main__":
    main()
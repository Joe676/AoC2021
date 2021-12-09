import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "17_input.txt")
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    lines = [line.rstrip() for line in lines]

    risk_sum = 0
    is_lowpoint = True

    for i, line in enumerate(lines):
        for j, height in enumerate(line):
            height = int(height)
            for i_off in range(-1, 2):
                for j_off in range(-1, 2):
                    if i_off == 0 and j_off == 0:
                        continue
                    if on_board(i+i_off, j+j_off, len(lines), len(line)):
                        if int(lines[i+i_off][j+j_off]) < height:
                            is_lowpoint = False
                            break
            if is_lowpoint:
                risk_sum += 1 + height
            is_lowpoint = True
    print(risk_sum)
                        

def on_board(x, y, max_x, max_y):
    return x >= 0 and x < max_x and y >= 0 and y < max_y

if __name__ == "__main__":
    main()
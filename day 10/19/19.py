import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "19_input.txt")
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    closing = {
        "(":")",
        "[":"]",
        "{":"}",
        "<":">"
    }
    points = {
        ")":3,
        "]":57,
        "}":1197,
        ">":25137
    }
    score = 0
    for line in lines:
        line = line.rstrip()
        open_chunks = []
        for c in line:
            if c in closing.keys():
                open_chunks.append(c)
            elif c == closing[open_chunks[-1]]:
                open_chunks = open_chunks[:-1]
            else:
                score += points[c]
                break
    print(score)


if __name__ == "__main__":
    main()
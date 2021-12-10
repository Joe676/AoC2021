import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "20_input.txt")
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
        ")":1,
        "]":2,
        "}":3,
        ">":4
    }
    scores = []
    for line in lines:
        score = 0
        line = line.rstrip()
        open_chunks = []
        corrupted = False
        for c in line:
            if c in closing.keys():
                open_chunks.append(c)
            elif c == closing[open_chunks[-1]]:
                open_chunks = open_chunks[:-1]
            else:
                corrupted = True
                break
        if corrupted:
            continue
        while len(open_chunks)>0:
            score *= 5
            score += points[closing[open_chunks[-1]]]
            open_chunks = open_chunks[:-1]
        scores.append(score)
    scores.sort()
    print(scores[(len(scores)-1)//2])


if __name__ == "__main__":
    main()
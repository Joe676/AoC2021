import os
from collections import Counter

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "27_input.txt")
    f = open(filename, 'r')
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

    N = 10

    template = lines[0]
    for _ in range(N):
        template_copy = template
        indexes = []
        for line in lines[2:]:
            pair, insert = line.split(' -> ')
            
            start=0
            while (idx := template[start:].find(pair)) > -1:
                idx += start
                # print('dddd', idx)
            # if (idx := template.find(pair)) > -1:
                lower_count = 0
                # print(idx, indexes)
                for i in indexes:
                    if i <= idx+lower_count:
                        lower_count+=1
                # print(pair, insert, '-', idx+lower_count)
                template_copy = template_copy[:idx+1+lower_count] + insert + template_copy[idx+1+lower_count:]
                indexes.append(idx+lower_count)
                start = idx+1
        template = template_copy
    print(template)
    c = Counter(template)
    best = ('', 0)
    worst = ('', len(template))
    for k, v in c.items():
        if (v>best[1]):
            best = (k, v)
        if (v<worst[1]):
            worst = (k, v)
    print(best[1] - worst[1])
        

if __name__ == "__main__":
    main()
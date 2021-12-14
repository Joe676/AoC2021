import os
from collections import Counter

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "28_input.txt")
    f = open(filename, 'r')
    lines = [l.rstrip() for l in f.readlines()]
    f.close()
    pairs = dict()
    
    for line in lines[2:]:
        pair, insert = line.split(' -> ')
        pairs[pair] = insert

    N = 40

    template = lines[0]

    sectors = {}
    for i in range(len(template)-1):
        if (t:=template[i:i+2]) not in sectors:
            sectors[t] = 0
        sectors[t]+=1
    
    for _ in range(N):
        sectors2 = dict()
        for sector in sectors:
            insert = pairs[sector]

            if (s := sector[0]+insert) not in sectors2:
                sectors2[s] = 0
            sectors2[s] += sectors[sector]
            
            if (s := insert + sector[1]) not in sectors2:
                sectors2[s] = 0
            sectors2[s] += sectors[sector]
        sectors = sectors2
    
    counter = dict()
    for s, v in sectors.items():
        if not s[0] in counter:
            counter[s[0]] = 0
        counter[s[0]] += v
    if not template[-1] in counter:
        counter[template[-1]] = 0
    counter[template[-1]]+=1
    print(max(counter.values()) - min(counter.values()))

if __name__ == "__main__":
    main()
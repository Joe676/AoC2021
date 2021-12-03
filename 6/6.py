'''
Solution for exercise 6 of Advent of Code 2021

Input is read into the lines array.
For each bit position the number of ones is counted. Then a new list of values is constructed
based on appropriate bit criteria.
'''

def main():
    f = open("5/5_input.txt", "r")
    lines = f.readlines()
    f.close()

    oxygen = 0
    co2 = 0
    ##oxygen
    lines2 = lines.copy()
    new_lines = []
    for pos in range(len(lines[0])-1):
        if len(lines2) == 1:
            oxygen = lines2[0]
            break
        ones = 0
        for line in lines2:
            ones += int(line[pos])
        for i in range(len(lines2)-1, -1, -1):
            if ones >= len(lines2)/2 and int(lines2[i][pos]) == 1:
                new_lines.append(lines2[i])
            elif ones < len(lines2)/2 and int(lines2[i][pos]) == 0:
                new_lines.append(lines2[i])
        lines2 = new_lines.copy()
        new_lines = []
        
    if len(lines2) == 1:
        oxygen = lines2[0]

    
    ##co2
    lines2 = lines.copy()
    new_lines = []
    for pos in range(len(lines[0])-1):
        if len(lines2) == 1:
            co2 = lines2[0]
            break

        ones = 0
        for line in lines2:
            ones += int(line[pos])
        for i in range(len(lines2)-1, -1, -1):
            if ones < len(lines2)/2 and int(lines2[i][pos]) == 1:
                new_lines.append(lines2[i])
            elif ones >= len(lines2)/2 and int(lines2[i][pos]) == 0:
                new_lines.append(lines2[i])
        lines2 = new_lines.copy()
        new_lines = []
        
    if len(lines2) == 1:
        co2 = lines2[0]
    
    return (bin2dec(oxygen), bin2dec(co2))

def bin2dec(num):
    n = len(num)-1
    out = 0
    for i in range(n):
        out += int(num[n-i-1])*2**i
    return out

if __name__ == "__main__":
    o, c = main()
    print(o, c, o*c)
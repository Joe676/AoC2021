"""
Solution for exercise 7 of Advent of Code 2021

After reading in the input each number is 'marked' in a mask of every board.
Each board is then evaluated and if it contains a bingo the score is calculated
"""

def main():
    f = open("7/7_input.txt", 'r')
    lines = f.readlines()
    f.close()
    nums = lines[0].rstrip().split(',')
    nums = [int(x) for x in nums]
    boards = []
    i = 2
    while i < len(lines):
        b = [[], [], [], [], []]
        m = []
        for j in range(5):
            m.append([0, 0, 0, 0, 0])
            line = lines[i+j].rstrip().split(' ')
            while line.__contains__(''):
                line.remove('')
            line = [int(x) for x in line]
            for x in line:
                b[j].append(x)
        boards.append([b, m])
        i+=6
    
    for num in nums:
        for j in range(len(boards)):
            board, mask = boards[j]
            idx = None
            for k in range(5):
                try:
                    idx = (k, board[k].index(num))
                except:
                    continue
            if idx != None:
                mask[idx[0]][idx[1]] = 1
            out = 0
            if checkBingo(mask):
                for a in range(5):
                    for b in range(5):
                        if not mask[a][b]:
                            out += board[a][b]
                return out, num, out*num
        
def checkBingo(mask):
    diag1 = []
    diag2 = []
    for i in range(5):
        if all(mask[i]):
            return True
        v = [x[i] for x in mask]
        if all(v):
            return True
        diag1.append(mask[i][i])
        diag2.append(mask[-i-1][i])
    return False
    

if __name__ == "__main__":
    print(main())
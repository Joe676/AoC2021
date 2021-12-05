"""
Solution of exercise 10 of Advent of Code 2021

After parsing the input each line segment is iterated over and each point it covers is counted using dictionary.
"""

def main():
    f = open("10/10_input.txt", 'r')
    lines = f.readlines()
    f.close()
    counter = {}

    for line in lines:
        line = line.rstrip()
        A, B = line.split(" -> ")
        A = tuple(int(a) for a in A.split(','))
        B = tuple(int(b) for b in B.split(','))
        if A[0] == B[0]:
            for y in range(A[1], B[1]+(1 if A[1]<B[1] else -1), 1 if A[1]<B[1] else -1):
                if (A[0], y) in counter:
                    counter[(A[0], y)] += 1
                else:
                    counter[(A[0], y)] = 1
        
        elif A[1] == B[1]:
            for x in range(A[0], B[0]+(1 if A[0]<B[0] else -1), 1 if A[0]<B[0] else -1):
                if (x, A[1]) in counter:
                    counter[(x, A[1])] += 1
                else:
                    counter[(x, A[1])] = 1
        else:
            if A[0] > B[0]:
                A, B = B, A
            x, y = A
            if A[1] > B[1]:
                for i in range(0, B[0]-A[0]+1):
                    if (x+i, y-i) in counter:
                        counter[(x+i, y-i)] += 1
                    else:
                        counter[(x+i, y-i)] = 1
            else:
                for i in range(0, B[0]-A[0]+1):
                    if (x+i, y+i) in counter:
                        counter[(x+i, y+i)] += 1
                    else:
                        counter[(x+i, y+i)] = 1
    count = 0
    for k, v in counter.items():
        if v >= 2:
            count += 1
    print(count)
    




if __name__ == "__main__":
    main()

    
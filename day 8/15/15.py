import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "15_input.txt")
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    count = 0
    for line in lines:
        digits = line.split(' | ')[1].rstrip().split(' ')
        for digit in digits:
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                count+=1
    print(count)

if __name__ == "__main__":
    main()
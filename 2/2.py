def main():
    f = open("2/2_input.txt", "r")
    lines = f.readlines()
    f.close()
    lines = [int(x) for x in lines]
    count = 0
    for i in range(len(lines)-2):
        count += 1 if sum(lines[i:i+3]) < sum(lines[i+1:i+4]) else 0
    print(count)

if __name__ == "__main__":
    main()
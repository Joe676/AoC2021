def main():
    f = open("1_input.txt", "r")
    count = 0
    lines = f.readlines()
    f.close()
    prev = int(lines[0])
    for line in lines[1:]:
        cur = int(line)
        if cur > prev:
            count += 1
        prev = cur
    print(count)

if __name__ == "__main__":
    main()
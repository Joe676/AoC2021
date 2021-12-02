f = open("3/3_input.txt", "r")
lines = f.readlines()
f.close()
x = 0
y = 0

for line in lines:
    line.rstrip()
    l = line.split(" ")
    print(l)
    opt = l[0]
    print(l[1])
    h = int(l[1])
    if opt == "forward":
        x+=h
    elif opt == "down":
        y+=h
    elif opt == "up":
        y-=h
print(x, y, x*y)
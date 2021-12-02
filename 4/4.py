f = open("4/4_input.txt", "r")
lines = f.readlines()
f.close()

aim = 0
x, y = 0, 0

for line in lines:
    line.rstrip()
    l = line.split(" ")
    opt = l[0]
    h = int(l[1])
    if opt == "forward":
        x+=h
        y+=h*aim
    elif opt == "down":
        aim+=h
    elif opt == "up":
        aim-=h
print(x, y, x*y)
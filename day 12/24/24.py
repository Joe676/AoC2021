import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "24_input.txt")
    f = open(filename, 'r')
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

    graph = dict()
    for line in lines:
        line.rstrip()
        a, b = line.split('-')
        if a in graph.keys():
            graph[a].append(b)
        else:
            graph[a] = [b]
        
        if b in graph.keys():
            graph[b].append(a)
        else:
            graph[b] = [a]

    count = 0
    stack = []
    stack.append((True, ['start']))
    while len(stack)>0:
        possible2, curRoute = stack.pop(0)
        curV = curRoute[-1]
        print(len(stack), count)
        if curV == 'end':
            count+=1
            continue
        for neighbor in graph[curV]:
            if neighbor.isupper() or (not neighbor in curRoute) or (possible2 and curRoute.count(neighbor)==1 and neighbor != 'start'):
                newRoute = curRoute.copy()
                newRoute.append(neighbor)
                if neighbor.islower() and newRoute.count(neighbor) == 2:
                    stack.append((False, newRoute))
                    continue
                stack.append((possible2, newRoute))

    print(count)



        

if __name__ == "__main__":
    main()
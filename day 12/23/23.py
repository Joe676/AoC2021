import os

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "23_input.txt")
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
    
    routes = []
    count = 0
    stack = []
    stack.append(['start'])
    while len(stack)>0:
        curRoute = stack.pop(0)
        curV = curRoute[-1]
        if curV == 'end' and curRoute not in routes:
            count+=1
            routes.append(curRoute)
            continue
        for neighbor in graph[curV]:
            if neighbor.isupper() or not neighbor in curRoute:
                newRoute = curRoute.copy()
                newRoute.append(neighbor)
                stack.append(newRoute)
    print(count)



        

if __name__ == "__main__":
    main()
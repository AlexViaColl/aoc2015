import sys

min_dist = sys.maxsize

def traverse(graph, visited, cost=0):
    global min_dist
    if len(graph) == len(visited):
        if cost < min_dist:
            min_dist = cost
        return
    current_node = visited[-1]
    for next_node in graph[current_node]:
        c = graph[current_node][next_node]
        if not next_node in visited:
            traverse(graph, [*visited, next_node], cost + c)

def solve(s):
    graph = {}
    for l in s.splitlines():
        org, _, dst, _, distance = l.split()
        distance = int(distance)
        if not org in graph:
            graph[org] = {dst: distance}
        else:
            graph[org][dst] = distance
        if not dst in graph:
            graph[dst] = {org: distance}
        else:
            graph[dst][org] = distance

    for k in graph:
        traverse(graph, [k])

    return min_dist

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()

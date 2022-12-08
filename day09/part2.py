import sys

max_dist = 0

def traverse(graph, visited, cost=0):
    global max_dist
    if len(graph) == len(visited):
        if cost > max_dist:
            max_dist = cost
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

    return max_dist

def main():
    with open('input.txt') as f:
        print(solve(f.read()))

if __name__ == '__main__':
    main()

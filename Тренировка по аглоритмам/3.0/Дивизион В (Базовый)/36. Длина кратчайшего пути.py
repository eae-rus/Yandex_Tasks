def main():
    
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        adjacency_matrix = list(map(int, input().split()))
        for j in range(n):
            if adjacency_matrix[j] == 1:
                graph[i+1].append(j+1)
                
    start_node, end_node = list(map(int, input().split()))
    distance_visited = [-1 for _ in range(n+1)]
    distance = 1
    next_visited = set()
    now_visited = set(graph[start_node])
    while len(now_visited) > 0 and distance_visited[end_node] == -1:
        for i in now_visited:
            if distance_visited[i] == -1:
                distance_visited[i] = distance
                for j in graph[i]:
                    if distance_visited[j] == -1:
                        next_visited.add(j)
        now_visited = next_visited
        next_visited = set()
        distance += 1
    print(distance_visited[end_node])
    
        
if __name__ == '__main__':
	main()
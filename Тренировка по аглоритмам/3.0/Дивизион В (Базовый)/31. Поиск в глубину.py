def main():
    def dfs(graph, node, visited):
        visited[node] = True
        for next_node in graph[node]:
            if not visited[next_node]:
                dfs(graph, next_node, visited)
    
    N, M = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        node_1, node_2 = list(map(int, input().split()))
        if node_1 != node_2:
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)
    
    visited = [False for _ in range(N+1)]
    dfs(graph, 1, visited)
    
    connectivity_components_count = 0
    connectivity_components = []
    for i in range(1, N+1):
        if visited[i]:
            connectivity_components.append(i)
            connectivity_components_count += 1
            
    print(connectivity_components_count)
    print(" ".join(map(str, connectivity_components)))
    
    
    
        
if __name__ == '__main__':
	main()

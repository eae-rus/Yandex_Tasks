import sys
# Установить новое значение глубины рекурсии на 10000
sys.setrecursionlimit(100000+100)

def main():
    def dfs(graph, node, visited, local_visited):
        visited[node] = True
        local_visited.append(node)
        for next_node in graph[node]:
            if not visited[next_node]:
                dfs(graph, next_node, visited, local_visited)
    
    N, M = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        node_1, node_2 = list(map(int, input().split()))
        if node_1 != node_2:
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)
    
    all_CC_count = [] # connectivity_components (CC)
    all_CC = [] # connectivity_components (CC)
    visited = [False for _ in range(N+1)]
    for i in range(1, N+1):
        if not visited[i]:
            local_visited = []
            dfs(graph, i, visited, local_visited)

            connectivity_components_count = 0
            connectivity_components = []
            for node in local_visited:
                connectivity_components.append(node)
                connectivity_components_count += 1
            
            all_CC_count.append(connectivity_components_count)
            all_CC.append(connectivity_components)

    print(len(all_CC_count))
    for i in range(len(all_CC_count)):
        print(all_CC_count[i])
        print(" ".join(map(str, all_CC[i])))
        
if __name__ == '__main__':
	main()

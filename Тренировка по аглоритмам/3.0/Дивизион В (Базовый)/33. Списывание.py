import sys
# Установить новое значение глубины рекурсии на 10000
sys.setrecursionlimit(100000+100)

def main():
    def dfs(graph, node, previous_node, visited, is_cycle_found):
        visited[node] = True
        for next_node in graph[node]:
            if not visited[next_node]:
                is_cycle_found = dfs(graph, next_node, node, visited, is_cycle_found)
            elif next_node != previous_node:
                is_cycle_found = True
            if is_cycle_found:
                break
        return is_cycle_found
    
    N, M = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        node_1, node_2 = list(map(int, input().split()))
        if node_1 != node_2:
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)
    
    is_cycle_found = False
    visited = [False for _ in range(N+1)]
    for i in range(1, N+1):
        if not visited[i]:
            is_cycle_found = dfs(graph, i, 0, visited, False)


    if is_cycle_found:
        print("NO")
    else:
        print("YES")
        
if __name__ == '__main__':
	main()

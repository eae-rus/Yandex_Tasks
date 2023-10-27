import sys
# Установить новое значение глубины рекурсии на 10000
sys.setrecursionlimit(100000+100)

def main():
    def dfs(graph, node, previous_node, visited, path):
        visited[node] = True
        path.append(node)

        for next_node in graph[node]:
            if not visited[next_node]:
                is_cycle_found, cycle_path = dfs(graph, next_node, node, visited, path)
                if is_cycle_found:
                    return [True, cycle_path]
            elif previous_node != next_node and next_node in path:
                # Найден цикл
                return [True, path]

        path.pop()
        return [False, path]
    
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        adjacency_matrix = list(map(int, input().split()))
        for j in range(n):
            if adjacency_matrix[j] == 1:
                graph[i+1].append(j+1)
    
    is_cycle_found = False
    cycle_path = []
    visited = [False for _ in range(n+1)]
    for i in range(1, n+1):
        if not visited[i]:
            is_cycle_found, cycle_path = dfs(graph, i, 0, visited, [])
            if is_cycle_found:
                is_cycle_found = True
                break

    if is_cycle_found:
        print("YES")
        print(len(cycle_path))
        print(" ".join(map(str, cycle_path)))
    else:
        print("NO")
        
if __name__ == '__main__':
	main()
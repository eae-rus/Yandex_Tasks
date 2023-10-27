import sys
# Установить новое значение глубины рекурсии на 10000
sys.setrecursionlimit(100000+100)

def main():
    def dfs(graph, node, visited, color):
        visited[node] = color

        next_color = color%2+1
        for next_node in graph[node]:
            if not visited[next_node]:
                if dfs(graph, next_node, visited, next_color):
                    return True
            elif visited[next_node] == color:
                # Найден неразделимость по двойному цвету
                return True
        return False
    
    N, M = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        node_1, node_2 = list(map(int, input().split()))
        if node_1 != node_2:
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)
    
    is_cycle_found = False
    visited = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        if not visited[i]:
            if dfs(graph, i, visited, 1):
                is_cycle_found = True
                break

    if is_cycle_found:
        print("NO")
    else:
        print("YES")
        
if __name__ == '__main__':
	main()

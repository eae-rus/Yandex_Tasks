def tsp_dp(adj_matrix):
    n = len(adj_matrix)
    INF = float('inf')

    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v) and u != v:
                    dp[mask][v] = min(dp[mask][v], dp[mask ^ (1 << v)][u] + adj_matrix[u][v])

    ans = INF
    for v in range(1, n):
        ans = min(ans, dp[(1 << n) - 1][v] + adj_matrix[v][0])

    return ans if ans != INF else -1

def main():
    '''
    '''
    N = int(input())
    adjacency_edges = [[0] * (N+1)]
    for _ in range(N):
        adjacency_edges.append([0] + list(map(int, input().split())))
    
    is_visited = [False] * (N+1)
    is_visited[0] = True
    node, sum_edge = 1, 0
    answer = 0
    if N > 1:
        answer = tsp_dp(adjacency_edges)
    print(answer)
    
if __name__ == '__main__':
    main()
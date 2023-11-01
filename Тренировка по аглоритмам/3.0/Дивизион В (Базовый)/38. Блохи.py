def main():
    def calculate_jump(node, variant):
        variants = {
            1: [node[0] - 2, node[1] + 1],
            2: [node[0] - 2, node[1] - 1],
            3: [node[0] - 1, node[1] - 2],
            4: [node[0] + 1, node[1] - 2],
            5: [node[0] + 2, node[1] - 1],
            6: [node[0] + 2, node[1] + 1],
            7: [node[0] + 1, node[1] + 2],
            8: [node[0] - 1, node[1] + 2]
        }
        return variants.get(variant, [node[0], node[1]])
        
    def is_valid_node(X, Y, N, M, visited_nodes):
        if X > 0 and X <= N and Y > 0 and Y <= M:
            if not visited_nodes[X][Y]:
                visited_nodes[X][Y] = True
                return True
        return False
    
    N, M, feeder_X, feeder_Y, Q  = list(map(int, input().split()))
    
    # считаем путь от кормушки до всех точек
    visited_nodes = [[False for _ in range(M+1)] for _ in range(N+1)]
    visited_distance = [[-1 for _ in range(M+1)] for _ in range(N+1)]
    visited_nodes[feeder_X][feeder_Y] = True
    visited_distance[feeder_X][feeder_Y] = 0
    distance = 1
    now_visited = []
    now_visited.append([feeder_X, feeder_Y])
    while len(now_visited) > 0:
        next_visited = []
        for k in range(len(now_visited)):
            node = now_visited[k]
            for variant in range(1, 9):
                jump = calculate_jump(node, variant)
                if is_valid_node(jump[0], jump[1], N, M, visited_nodes):
                    next_visited.append(jump)
                    visited_distance[jump[0]][jump[1]] = distance
        now_visited = next_visited
        distance += 1

    # считаем суммарный путь от блох точек до кормушки
    all_distance = 0
    is_valid = True
    for _ in range(Q):
        fleas_X, fleas_Y = list(map(int, input().split()))
        if visited_distance[fleas_X][fleas_Y] == -1 or not is_valid:
            all_distance = -1
            is_valid = False
        else:
            all_distance += visited_distance[fleas_X][fleas_Y]
        
    print(all_distance)
    
    
if __name__ == '__main__':
	main()
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
    all_distance = 0
    
    fleas = []
    for _ in range(Q):
        fleas_X, fleas_Y = list(map(int, input().split()))
        fleas.append([fleas_X, fleas_Y])
    
    for i in range(Q):
        fleas_X, fleas_Y = fleas[i][0], fleas[i][1]
        if fleas_X == feeder_X and fleas_Y == feeder_Y:
            continue

        visited_nodes = [[False for _ in range(M+1)] for _ in range(N+1)]
        visited_nodes[fleas_X][fleas_Y] = True
        
        distance = 1
        now_visited = []
        now_visited.append([feeder_X, feeder_Y])
        is_feeder_found = False
        while len(now_visited) > 0 and not is_feeder_found:
            next_visited = []
            for k in range(len(now_visited)):
                node = now_visited[k]
                for variant in range(1, 9):
                    jump = calculate_jump(node, variant)
                    if is_valid_node(jump[0], jump[1], N, M, visited_nodes):
                        next_visited.append(jump)
                        
                    if jump[0] == fleas_X and jump[1] == fleas_Y:
                        all_distance += distance
                        is_feeder_found = True
                        break
                if is_feeder_found:
                    break
            now_visited = next_visited
            distance += 1

        if not is_feeder_found:
            all_distance = -1
            break
            
        
    print(all_distance)
    
    
if __name__ == '__main__':
	main()
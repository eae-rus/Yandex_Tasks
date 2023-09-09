def main():
    '''
    '''
    sum_count = int(input())
    vagons = list(map(int, input().split()))
    
    now_vagon = 0
    stack_vagon = []
    stack_vagon.append(vagons[0])
    is_real = True
    for vagon in vagons[1:]:
        if vagon < stack_vagon[-1]:
            stack_vagon.append(vagon)
        else:
            while stack_vagon and vagon > stack_vagon[-1]:
                new_vagon = stack_vagon.pop()
                if now_vagon + 1 == new_vagon:
                    now_vagon += 1
                else:
                    is_real = False
                    break
                
            if not is_real or not stack_vagon:
                break
            stack_vagon.append(vagon)

    for _ in range(len(stack_vagon)):
        new_vagon = stack_vagon.pop()
        if now_vagon + 1 == new_vagon:
            now_vagon += 1
        else:
            is_real = False
            break
    
    if is_real:
        print("YES")
    else:
        print("NO")
        
if __name__ == '__main__':
	main()
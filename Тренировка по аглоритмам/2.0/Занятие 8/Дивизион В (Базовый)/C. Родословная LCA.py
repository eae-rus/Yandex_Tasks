import sys

def main():
    '''
    '''
    N = int(input())
    child_to_parant_dict = {}
    for i in range(N-1):
        descendant, parent = input().split()
        child_to_parant_dict[descendant] = parent     

    answer = []
    query = sys.stdin.readline()[0:-1].split(" ")
    while not (query == ""):
        try:
            descendant, parent = query[0], query[1]
        except:
            break
        
        ancestors = set()
        parent_i = descendant
        ancestors.add(parent_i)
        while parent_i in child_to_parant_dict:
            parent_i = child_to_parant_dict[parent_i]
            ancestors.add(parent_i)
            
        parent_i = parent
        while parent_i not in ancestors:
            parent_i = child_to_parant_dict[parent_i]
            
        answer.append(parent_i)
        query = sys.stdin.readline()[0:-1].split(" ")
        
    print(' '.join(map(str, answer)))
     
if __name__ == '__main__':
	main()
    
if __name__ == '__main__':
	main()
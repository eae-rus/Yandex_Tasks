def main():
    '''
    '''
    polish_abstract = input().split()
    stack_story = []
    for symbol in polish_abstract:
        if symbol == "+":
           stack_story.append(stack_story.pop() + stack_story.pop())
        elif symbol == "-":
           stack_story.append(-stack_story.pop() + stack_story.pop())
        elif symbol == "*":
           stack_story.append(stack_story.pop() * stack_story.pop())
        else:
           stack_story.append(int(symbol)) 
    
    print(stack_story.pop())
        
if __name__ == '__main__':
	main()
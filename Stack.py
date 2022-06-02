# Arly Mae Bandong
def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack)== 0

def push(stack,item):
    stack.append(item)
    print("pushed item:" + item)

def pop(stacked):
    if (check_empty(stack)):
        return "stack is Empty"

    return stack.pop()

stack = create_stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
push(stack,str(5))
print("popped item;"+pop(stack))
print("stack after popping an element:"+str(stack))

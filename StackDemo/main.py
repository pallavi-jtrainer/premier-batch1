# stack implementation

# create the stack
def create_stack():
    stack = []
    return stack


# check if stack is empty
def check_stack_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("Added Element: " + item)


def pop(stack):
    if check_stack_empty(stack):
        return "Stack is Empty"

    return stack.pop()


stack1 = create_stack()
push(stack1, str(1))
push(stack1, str(3))
push(stack1, str(4))

print("popped element: " + pop(stack1))
print("after popping: " + str(stack1))

print("popped element: " + pop(stack1))
print("popped element: " + pop(stack1))
print("popped element: " + pop(stack1))

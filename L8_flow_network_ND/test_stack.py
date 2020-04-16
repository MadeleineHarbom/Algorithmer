from _collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')

print("The stack")
print(stack)

print('first pop:')
print(stack.pop())
print('second pop')
print(stack.pop())


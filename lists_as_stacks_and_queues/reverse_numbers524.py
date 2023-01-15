integers = input().split()
# integers = list(map(int, input().split()))
stack = []
for i in range(len(integers)):
    stack.append(integers.pop())
print(' '.join(stack))
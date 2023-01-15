stack = []
my_int = int(input())

map_functions = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}
for i in range(my_int):
    query = list(map(int, input().split()))
    map_functions[query[0]](query)
stack.reverse()
print(*stack, sep=', ')

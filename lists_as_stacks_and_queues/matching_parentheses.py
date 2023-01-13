def matching_parentheses(the_str):
    parenthesis = []
    for i in range(len(the_str)):
        symbol = the_str[i]
        if symbol == "(":
            parenthesis.append(i)
        elif symbol == ")":
            start_index = parenthesis.pop()
            print(the_str[start_index:i+1])


inp = input()
matching_parentheses(inp)
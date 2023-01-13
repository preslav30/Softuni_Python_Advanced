def matching_parentheses(the_str):
    parenthesis = []
    for i in range(len(the_str)):
        if the_str[i] == "(":
            parenthesis.append(i)
        elif the_str[i] == ")":
            start_index = parenthesis.pop()
            print(the_str[start_index:i+1])


inp = input()
matching_parentheses(inp)
from collections import deque

text = deque(input().split())
main_colors = 'red', 'yellow', 'blue'
secondary_colors = 'orange', 'purple', 'green'
found_main = []
found_secondary = []
found_final = []
while text:
    if len(text) == 1:
        if text[0] in main_colors or text[0] in secondary_colors:
            found_final.append(text[0])
        break

    try_color1 = text[0] + text[-1]
    try_color2 = text[-1] + text[0]
    if try_color1 in main_colors:
        found_final.append(try_color1)
        text.remove(text[0])
        text.remove(text[-1])
    elif try_color1 in secondary_colors:
        found_final.append(try_color1)
        text.remove(text[0])
        text.remove(text[-1])


    elif try_color2 in main_colors:
        found_final.append(try_color2)
        text.remove(text[0])
        text.remove(text[-1])
    elif try_color2 in secondary_colors:
        found_final.append(try_color2)
        text.remove(text[0])
        text.remove(text[-1])


    elif try_color1 not in main_colors and try_color1 not in secondary_colors and try_color2 not in main_colors and try_color2 not in secondary_colors:
        text[0] = text[0][:-1]
        text[-1] = text[-1][:-1]
        popped_first = text.popleft()
        popped_last = text.pop()
        if len(text) % 2 == 0:
            text.insert((len(text) // 2), popped_first)
            text.insert((len(text) // 2) + 1, popped_last)
        else:
            text.insert((len(text) // 2) + 1, popped_first)
            text.insert((len(text) // 2) + 2, popped_last)
        if len(popped_first) == 0:
            text.remove(popped_first)
        if len(popped_last) == 0:
            text.remove(popped_last)

for color in found_final:
    if color == 'orange':
        if ('red' not in found_final) or ('yellow' not in found_final):
            found_final.remove(color)
    elif color == 'purple':
        if ('red' not in found_final) or ('blue' not in found_final):
            found_final.remove(color)
    elif color == 'green':
        if ('blue' not in found_final) or ('yellow' not in found_final):
            found_final.remove(color)
print(found_final)
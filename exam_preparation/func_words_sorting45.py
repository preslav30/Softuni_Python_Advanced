def words_sorting(*words):
    words_dict = {}
    for word in words:
        ascii_sum = 0
        if word not in words_dict.keys():
            for ch in word:
                ascii_sum += ord(ch)
            words_dict[word] = ascii_sum
    total_sum = sum(words_dict.values())
    words_dict = dict(sorted(words_dict.items(), key=lambda x: (-x[1] if total_sum % 2 != 0 else x[0])))
    result = []
    for k, v in words_dict.items():
        result.append(f'{k} - {v}')
    return '\n'.join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print()
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print()
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))


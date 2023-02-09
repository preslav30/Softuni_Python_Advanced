def concatenate(*args, **kwargs):
    concat = ''
    for arg in args:
        concat += arg
    for key, value in kwargs.items():
        if key in concat:
            start = concat.index(key[0])
            end = concat.index(key[-1]) + 1
            concat = concat[:start] + value + concat[end:]
    return concat


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

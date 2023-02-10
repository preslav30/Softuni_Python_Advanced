def age_assignment(*args, **kwargs):
    output = ''
    for name in sorted(args):
        for key, value in kwargs.items():
            if key == name[0]:
                output += f'{name} is {value} years old.\n'

    return output



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


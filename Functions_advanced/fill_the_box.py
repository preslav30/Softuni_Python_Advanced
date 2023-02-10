def fill_the_box(height, length, width, *cubes,):
    cubes = list(cubes)
    finish_index = cubes.index('Finish')
    end = False
    no_space = False
    space_filled = 0
    volume = height * width * length
    starting_index_of_cubes_left = 0

    for i in range(len(cubes)):
        cube = cubes[i]
        if cubes[i] == 'Finish':
            break
        elif space_filled + cubes[i] > volume:
            starting_index_of_cubes_left = cubes.index(cubes[i])
            cubes[i] = (space_filled + cubes[i]) - volume
            space_filled = volume
            no_space = True
            break

        else:
            space_filled += cubes[i]

    if no_space:
        sum_of_cubes_left = sum(cubes[starting_index_of_cubes_left:finish_index])
        return f'No more free space! You have {sum_of_cubes_left} more cubes.'
    else:
        return f'There is free space in the box. You could put {volume - space_filled} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))


clothes = list(map(int, input().split()))
one_rack_capacity = int(input())
done = False
number_of_racks = 1
while clothes:
    current_rack = one_rack_capacity
    while current_rack > 0:
    # while clothes and current_rack > 0:
        last_piece = clothes[-1]
        if current_rack - last_piece == 0:
            current_rack -= last_piece
            clothes.pop()
            if len(clothes) > 0:
                number_of_racks += 1
                break
            else:
                done = True
                break
        elif current_rack - last_piece < 0:
            number_of_racks += 1
            break
        elif current_rack - last_piece > 0:
            current_rack -= last_piece
            clothes.pop()
            if not clothes:
                break
        if done:
            break
print(number_of_racks)

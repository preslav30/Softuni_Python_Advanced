def neg_pos(sequence):
    def map_to_int():
        integers = list(map(int, sequence.split()))
        return integers

    def separate_neg_from_pos():
        neg, pos = [], []
        for num in map_to_int():
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        return neg, pos

    def sum_neg_pos():
        neg, pos = separate_neg_from_pos()
        suma_neg = sum(neg)
        suma_pos = sum(pos)
        return suma_neg, suma_pos

    def print_func():
        abs_neg, abs_pos = sum_neg_pos()
        print(abs_neg)
        print(abs_pos)
        if abs(abs_neg) > abs_pos:
            print("The negatives are stronger than the positives")
        else:
            print("The positives are stronger than the negatives")

    return print_func()


neg_pos(input())

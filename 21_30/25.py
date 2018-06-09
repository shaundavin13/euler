import itertools


def get_fibonacci_generator():
    # Normally, fibonacci sequences start with 1, 1, 2, 3, 5, etc.
    # This omits the first "1" but that's okay since 1 is odd.
    first_previous_value = 0
    second_previous_value = 1
    for _ in itertools.count():
        first_previous_value, second_previous_value = second_previous_value, first_previous_value + second_previous_value
        yield second_previous_value


def first_fibonacci_with_n_digits(n):

    gen = get_fibonacci_generator()

    idx = 1
    num = 2
    while len(str(num)) < n:
        num = next(gen)
        idx += 1
    return idx


answer = first_fibonacci_with_n_digits(1000
                                       )
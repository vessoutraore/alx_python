def fibonacci_sequence(n):
    if n <= 0:
        return []

    array = [0, 1]

    while len(array) < n:
        next = array[-1] + array[-2]
        array.append(next)
    return array[:n] 
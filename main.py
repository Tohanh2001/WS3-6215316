def serial_sum(n, m=None):
    if m is None:
        return sum(range(1, n + 1))
    else:
        return sum(range(n, m + 1))


# Test the function with two sets of inputs
print(serial_sum(4))  # Output: 10
print(serial_sum(2, 4))  # Output: 9

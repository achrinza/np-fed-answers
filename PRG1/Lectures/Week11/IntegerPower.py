def integer_power(base: int, exponent: int) -> int:
    result = 1

    for i in range(exponent):
        result *= base

    return result

print(integer_power(3, 4))

import math


def power(a, b):
    print(f"Calculating {a} to the power of {b}....")
    return a**b


def modulus(a, b):
    print(f"Calculating {a} modulus {b}......")
    return a % b


def floor1(a, b):
    print(f"Calculating the floor value of {a} divided by {b}")
    return math.floor(a / b)


squared = power(6, 8)
mod = modulus(23, 8)
floor_base = floor1(53, 11)

print(
    f"The value of the power calculation is: {squared}, the modulus is: {mod} and the floor value is: {floor_base}"
)

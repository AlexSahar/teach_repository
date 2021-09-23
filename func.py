def show(txt):
    symbl = list(sorted(txt))
    print(symbl)


def kv(n):
    return n ** 2


def sqsum(n):
    nums = [k * k for k in range(1, n + 1)]
    return sum(nums)


show("Python")

print(f"Квадрат числа 4 равен {kv(4)}")
print(f"Сумма натуральных Квадратов числа от 1 до 4 равен {sqsum(4)}")

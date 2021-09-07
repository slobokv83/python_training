import math

def change(num):
    x = math.floor(num / 10)
    num1 = num - x * 10
    y = math.floor(num1 / 5)
    num2 = num1 - y * 5
    z = math.floor(num2 / 2)
    num3 = num2 - z * 2

    if (num3 == 0):
        return {"two": z, "five": y, "ten": x}
    else:
        return math.nan

print(change(126))
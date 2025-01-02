def function_with_uncommon_error(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        return x / y

result = function_with_uncommon_error(0, 0)
print(result)
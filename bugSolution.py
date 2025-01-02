def function_with_uncommon_error_solution(x, y):
    if x == 0 and y == 0:
        return 0
    elif x == 0:
        return y
    elif y == 0:
        return x
    else:
        return x / y

result = function_with_uncommon_error_solution(0, 0)
print(result) 
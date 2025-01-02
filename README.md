# Python: ZeroDivisionError in Conditional Return Statement

This repository demonstrates a subtle bug that can lead to a `ZeroDivisionError` in Python, even when the function appears to handle cases where division by zero could occur.

## The Bug

The function `function_with_uncommon_error` attempts to handle cases where either `x` or `y` is 0 by returning the other variable. However, if both `x` and `y` are 0, the `else` block is executed, resulting in division by zero, even though the function is guarded against this case in if and elif block.

## The Solution

The solution modifies the function to explicitly check if both `x` and `y` are 0, returning 0 in that case.
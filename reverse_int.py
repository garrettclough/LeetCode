def reverse(self, x):
    result, isPos = 0, 1
    if x < 0:
        isPos = -1
        x = -1 * x
    while x != 0:
        result = result * 10 + x % 10
        if result > 2147483647:
            return 0
        x /= 10
    return result * isPos
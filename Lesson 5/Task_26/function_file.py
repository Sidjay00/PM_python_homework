def exp(num1, num2):
        if num2 == 0:
            return 1
        else:
            return num1 * exp(num1, num2-1)
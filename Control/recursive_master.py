def fibonaci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)


def factorial(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return n*factorial(n-1)


print(fibonaci(3))
print(factorial(5))
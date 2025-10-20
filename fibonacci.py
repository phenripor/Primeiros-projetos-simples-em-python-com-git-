def fibonacci(a,b):
    a,b = 0,1
    for _ in range(n):
        a, b = b, a + b

howmany = int(input("How many terms would you like?"))
fibonacci(howmany)
    
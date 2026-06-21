def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Ingresa un número: "))
print("Fibonacci:", fibonacci(num))
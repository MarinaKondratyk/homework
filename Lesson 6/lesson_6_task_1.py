def fibonacci(n):
    fibonacci_1 = 0
    fibonacci_2 = 1
    for _ in range(n-2):
        sequence_fibonacci = fibonacci_1 + fibonacci_2
        fibonacci_1 = fibonacci_2
        fibonacci_2 = sequence_fibonacci
    return sequence_fibonacci

print(fibonacci(10))




def fibonacci_terms(n_terms):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n_terms):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage: Print the first 10 Fibonacci numbers
n_terms = 10
fib_numbers = fibonacci_terms(n_terms)
print(f"The first {n_terms} Fibonacci numbers: {fib_numbers}")

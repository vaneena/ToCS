def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence[:n]

# Example usage
n_terms = 10
print(f"Fibonacci sequence with {n_terms} terms:", fibonacci(n_terms))

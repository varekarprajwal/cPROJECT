from benchmark import performance_decorator, print_performance_results, print_profiling_results

@performance_decorator
def say_hello():
    print("Hello!")

@performance_decorator
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    return result

@performance_decorator
def multiply_numbers(a, b):
    result = a * b
    print(f"The product of {a} and {b} is {result}")
    return result

if __name__ == "__main__":
    # Run functions (decorators will collect performance and profiling data automatically)
    say_hello()
    add_numbers(10, 20)
    multiply_numbers(5, 7)

    # Print the performance results in table format
    print_performance_results()

    # Print the profiling results
    print_profiling_results()

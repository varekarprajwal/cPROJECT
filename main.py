# main.py

from Benchmark import performance_decorator, print_performance_results, print_profiling_results, save_benchmark_results
from Benchmark import get_logger

# Get logger
logger = get_logger()

@performance_decorator
def say_hello():
    logger.info("say_hello function called")
    print("Hello!")

@performance_decorator
def add_numbers(a, b):
    logger.info(f"add_numbers called with a={a}, b={b}")
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    return result

if __name__ == "__main__":
    # Run functions (decorators will collect performance and profiling data automatically)
    say_hello()
    add_numbers(10, 20)
    
    # Save the results to a text file
    save_benchmark_results()

# main.py
from Benchmark import profile_function
import sys

# Function 1 to profile
@profile_function(str(sys.argv[1]))
def function_one():
    x = 0
    for i in range(5000):
        x += i
    return x

def main():
    # Run functions using cProfile profiling
    function_one()

    
    
if __name__ == '__main__':
    main()


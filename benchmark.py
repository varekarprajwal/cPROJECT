import time
import tracemalloc
import cProfile
import pstats
from tabulate import tabulate
from io import StringIO

# List to store performance data
performance_results = []
profiling_results = []

def performance_decorator(func):
    def wrapper(*args, **kwargs):
        # Start tracking memory
        tracemalloc.start()
        
        # Record start time
        start_time = time.time()
        
        # Profile the function execution
        pr = cProfile.Profile()
        pr.enable()
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        # Stop profiling
        pr.disable()
        
        # Record end time
        end_time = time.time()
        
        # Stop tracking memory and get the stats
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Collect performance data
        performance_data = {
            "Function": func.__name__,
            "Time Taken (seconds)": f"{end_time - start_time:.6f}",
            "Current Memory (MB)": f"{current / 10**6:.6f}",
            "Peak Memory (MB)": f"{peak / 10**6:.6f}"
        }
        performance_results.append(performance_data)
        
        # Collect profiling data
        prof_data = StringIO()
        stats = pstats.Stats(pr, stream=prof_data)
        stats.strip_dirs().sort_stats('time').print_stats()
        profiling_data = {
            "Function": func.__name__,
            "Profiling Data": prof_data.getvalue()
        }
        profiling_results.append(profiling_data)
        
        return result
    
    return wrapper

def print_performance_results():
    # Print the performance results in table format
    print("Performance Results:")
    print(tabulate(performance_results, headers="keys", tablefmt="grid"))

def print_profiling_results():
    # Print the profiling results in a separate table
    print("\nProfiling Results:")
    for result in profiling_results:
        print(f"\nFunction: {result['Function']}")
        print(result['Profiling Data'])

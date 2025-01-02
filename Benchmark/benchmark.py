import cProfile
from line_profiler import LineProfiler
import functools
from memory_profiler import memory_usage, profile
import io
import pstats
from contextlib import redirect_stdout

# Wrapper function for profiling
def profile_function(profiler_type='none', output_file='Benchmark/profile_results.txt'):
    """
    A wrapper function to profile a function using cProfile, line_profiler, or memory_profiler.
    :param profiler_type: 'cProfile', 'line_profiler', 'memory_profiler', or 'none' (for no profiling)
    :param output_file: The file where profiling results will be stored
    :return: a wrapped function with profiling enabled or no profiling
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None  # Ensure 'result' is always defined
            
            # Open the output file in write mode (this will clear previous content)
            with open(output_file, 'w') as f:  # 'w' mode clears the previous file contents
                if profiler_type == 'cProfile':
                    f.write(f"\nProfiling function '{func.__name__}' with cProfile...\n")
                    
                    # Create a profiler object
                    profiler = cProfile.Profile()
                    profiler.enable()

                    # Call the function
                    result = func(*args, **kwargs)
                    
                    # Disable profiler and capture the stats
                    profiler.disable()
                    
                    # Redirect the profiler stats to a string buffer
                    stream = io.StringIO()
                    stats = pstats.Stats(profiler, stream=stream)
                    stats.strip_dirs()
                    stats.sort_stats('cumulative')
                    stats.print_stats()

                    # Write the stats to the output file
                    f.write(stream.getvalue())

                elif profiler_type == 'line_profiler':
                    f.write(f"\nProfiling function '{func.__name__}' with line_profiler...\n")
                    profiler = LineProfiler()
                    profiler.add_function(func)
                    profiler.enable_by_count()
                    result = func(*args, **kwargs)
                    profiler.disable_by_count()
                    profiler.print_stats(stream=f)

                elif profiler_type == 'memory_profiler':
                    f.write(f"\nProfiling memory usage for function '{func.__name__}'...\n")
                    
                    # Capture memory profiler output using StringIO
                    mem_output = io.StringIO()
                    with redirect_stdout(mem_output):
                        # Use memory_profiler to track memory usage at a line-by-line level
                        @profile
                        def wrapped_func():
                            return func(*args, **kwargs)
                        
                        # Run the function and capture memory profile output
                        wrapped_func()

                    # Write the memory profiler output to the file
                    f.write(mem_output.getvalue())
                    
                else:
                    # No profiling, just run the function normally
                    f.write(f"\nRunning function '{func.__name__}' without profiling...\n")
                    result = func(*args, **kwargs)
                    
            return result  # Return the result of the function

        return wrapper
    return decorator

import time
import tracemalloc
import cProfile
import pstats
from io import StringIO
import asyncio
import psutil
import gc
import json
from tabulate import tabulate
import streamlit as st

# List to store performance data and profiling results
performance_results = []
profiling_results = []

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def performance_decorator(func):
    async def async_wrapper(*args, **kwargs):
        # Start tracking memory
        tracemalloc.start()

        # Record start time
        start_time = time.time()

        # Profile the function execution
        pr = cProfile.Profile()
        pr.enable()

        cpu_before = get_cpu_usage()

        # Execute the original function
        result = await func(*args, **kwargs)

        # Stop profiling
        pr.disable()
        end_time = time.time()

        cpu_after = get_cpu_usage()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        performance_data = {
            "Function": func.__name__,
            "Time Taken (seconds)": f"{end_time - start_time:.6f}",
            "Current Memory (MB)": f"{current / 10**6:.6f}",
            "Peak Memory (MB)": f"{peak / 10**6:.6f}",
            "CPU Usage Before (%)": cpu_before,
            "CPU Usage After (%)": cpu_after
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

    def sync_wrapper(*args, **kwargs):
        # Same implementation as async but for sync functions
        tracemalloc.start()
        start_time = time.time()

        pr = cProfile.Profile()
        pr.enable()

        cpu_before = get_cpu_usage()

        result = func(*args, **kwargs)

        pr.disable()
        end_time = time.time()

        cpu_after = get_cpu_usage()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        performance_data = {
            "Function": func.__name__,
            "Time Taken (seconds)": f"{end_time - start_time:.6f}",
            "Current Memory (MB)": f"{current / 10**6:.6f}",
            "Peak Memory (MB)": f"{peak / 10**6:.6f}",
            "CPU Usage Before (%)": cpu_before,
            "CPU Usage After (%)": cpu_after
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

    # Check if function is async or not
    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper

def print_performance_results():
    print("Performance Results:")
    print(tabulate(performance_results, headers="keys", tablefmt="grid"))

def print_profiling_results():
    print("\nProfiling Results:")
    for result in profiling_results:
        print(f"\nFunction: {result['Function']}")
        print(result['Profiling Data'])

def save_results():
    # Open the file in write mode
    with open('Benchmark/performance_results.txt', 'w') as f:
        # Write Performance Results Table
        f.write("=== Performance Results ===\n")
        
        # Format the performance results into a table
        table = tabulate(performance_results, headers="keys", tablefmt="grid")
        
        # Write the table to the file
        f.write(table)
        f.write("\n\n")

        # Write Profiling Results
        f.write("\n=== Profiling Results ===\n")
        for result in profiling_results:
            f.write(f"Function: {result['Function']}\n")
            f.write(f"Profiling Data:\n")
            f.write(result['Profiling Data'])
            f.write("\n\n")


def show_results():
    pass

def check_memory_leaks():
    # Detect memory leaks using the gc module
    gc.collect()
    print(f"Unreachable objects: {gc.garbage}")

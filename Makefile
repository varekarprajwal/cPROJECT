# Define variables
PYTHON = python3
VENV_DIR = venv
REQUIREMENTS = requirements.txt
EXECUTION = execution.txt
BENCHMARK_DIR = Benchmark
SCRIPT = main.py

# Default target to create and activate the virtual environment, install dependencies, and run the program
all: setup run

# Create virtual environment
$(VENV_DIR):
	$(PYTHON) -m venv $(VENV_DIR)

# Install dependencies in the virtual environment
install: $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)

# Run the Python program with detailed time and memory stats
run: $(VENV_DIR)
	/usr/bin/time -v $(VENV_DIR)/bin/python $(SCRIPT) none 2> $(EXECUTION)

run_cProfile: $(VENV_DIR)
	/usr/bin/time -v $(VENV_DIR)/bin/python $(SCRIPT) cProfile 2> $(EXECUTION)

run_line_profiler: $(VENV_DIR)
	/usr/bin/time -v $(VENV_DIR)/bin/python $(SCRIPT) line_profiler 2> $(EXECUTION)

run_memory_profiler: $(VENV_DIR)
	/usr/bin/time -v $(VENV_DIR)/bin/python $(SCRIPT) memory_profiler 2> $(EXECUTION)

# Setup the virtual environment and install dependencies
setup: $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)

# Clean up the virtual environment
clean:
	rm -rf $(VENV_DIR)

# Clear the log file
clear_logs:
	rm -f $(BENCHMARK_DIR)/logs/program.log

# To create a requirements file (e.g., if you want to track your Python dependencies)
freeze:
	$(VENV_DIR)/bin/pip freeze > $(REQUIREMENTS)

# Help command for displaying Makefile usage
help:
	@echo "Makefile for managing the Python project"
	@echo "Usage:"
	@echo "  make setup  	 		- Set up the virtual environment and install dependencies"
	@echo "  make run    			- Run the Python script without Profile"
	@echo "  make run_cProfile   		- Run the Python script with cProfile"
	@echo "  make run_line_profiler        - Run the Python script with line_profiler"
	@echo "  make run_memory_profiler      - Run the Python script with memory_profiler"
	@echo "  make clean   			- Remove the virtual environment"
	@echo "  make freeze 			- Generate a requirements.txt from the virtual environment"
	@echo "  make clear_ogs 		- Clear the log file (project_log.log)"

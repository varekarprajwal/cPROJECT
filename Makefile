# Define variables
PYTHON = python3
VENV_DIR = venv
REQUIREMENTS = requirements.txt
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
	/usr/bin/time -v $(VENV_DIR)/bin/python $(SCRIPT)

# Setup the virtual environment and install dependencies
setup: $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)

# Clean up the virtual environment
clean:
	rm -rf $(VENV_DIR)

# To create a requirements file (e.g., if you want to track your Python dependencies)
freeze:
	$(VENV_DIR)/bin/pip freeze > $(REQUIREMENTS)

# Help command for displaying Makefile usage
help:
	@echo "Makefile for managing the Python project"
	@echo "Usage:"
	@echo "  make setup   - Set up the virtual environment and install dependencies"
	@echo "  make run     - Run the Python script with time and memory statistics"
	@echo "  make clean   - Remove the virtual environment"
	@echo "  make freeze  - Generate a requirements.txt from the virtual environment"

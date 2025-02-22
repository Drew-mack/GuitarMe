import subprocess

def run_first_program():
    # Run the first program in its virtual environment
    subprocess.run(["./venv/bin/python", "Test.py"])  # macOS/Linux
    # subprocess.run(["venv_first\\Scripts\\python.exe", "run_first.py"])  # Windows

def run_second_program():
    # Run the second program in its virtual environment
    subprocess.run(["./venv_gp/bin/python", "MidiConverter.py"])  # macOS/Linux
    # subprocess.run(["venv_second\\Scripts\\python.exe", "run_second.py"])  # Windows

if __name__ == "__main__":
    run_first_program()
    run_second_program()
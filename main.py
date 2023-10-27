import subprocess
import os

def run_cache_script():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    cached_script_path = os.path.join(current_directory, "library\pycache\cached\dist\cache.py")

    try:
        subprocess.run(["python", cached_script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running cached.py: {e}")
    except FileNotFoundError:
        print("cached.py not found")

def main_program():
    # Your main program logic here
    print("Main program running...")

if __name__ == '__main__':
    run_cache_script()
    main_program()
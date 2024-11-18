import sys
from datetime import datetime

def main():
    # Echo command line arguments if any exist
    if len(sys.argv) > 1:
        print("\nCommand line arguments:")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"Argument {i}: {arg}")
        print()  # Empty line for better formatting
    
    # Write to stdout (standard output)
    print("This is a normal message going to stdout")
    print(f"Current time is: {datetime.now()}")
    
    # Write to stderr (standard error)
    print("This is an error message going to stderr", file=sys.stderr)
    print("Another error occurred!", file=sys.stderr)
    
    # You can also use sys.stdout and sys.stderr directly
    sys.stdout.write("Direct write to stdout\n")
    sys.stderr.write("Direct write to stderr\n")

if __name__ == "__main__":
    main()

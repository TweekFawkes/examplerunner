import sys
from datetime import datetime
import os

def main():
    # Echo command line arguments if any exist
    if len(sys.argv) > 1:
        print("\n[*] Command line arguments:")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"[*] Argument {i}: {arg}")
        print()  # Empty line for better formatting
    
    # Write to stdout (standard output)
    print("[*] This is a normal message going to stdout")
    print(f"[*] Current time is: {datetime.now()}")
    
    # Write to stderr (standard error)
    print("[*] This is an error message going to stderr", file=sys.stderr)
    print("[*] Another error occurred!", file=sys.stderr)
    
    # You can also use sys.stdout and sys.stderr directly
    sys.stdout.write("[*] Direct write to stdout\n")
    sys.stderr.write("[*] Direct write to stderr\n")
    
    # Print environment variables
    print("\n[*] Environment Variables:")
    for key, value in os.environ.items():
        print(f"[*] {key}={value}")
    
    # ... existing code ...

if __name__ == "__main__":
    main()

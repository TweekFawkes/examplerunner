import sys
from datetime import datetime
import os
import secrets

# [*] Default Environment Variables:
# PWD=/tmp/msmowz/20241121173033774104/001
# OLDPWD=/var/task
# LC_CTYPE=C.UTF-8

# [*] Creator Defined Environment Variables:
# SOMETHING=value

def load_wordlist(filename='eff_large_wordlist_002.txt'):
    try:
        with open(filename, 'r') as file:
            # Read words, strip whitespace, and filter out empty lines
            return [word.strip() for word in file.readlines() if word.strip()]
    except FileNotFoundError:
        # Fallback to default words if file not found
        return ['Himself', 'Warm', 'Deal', 'Object', 'Book', 'Wife', 'Seven', 'Uranus', 'Forget', 
                'Table', 'Chair', 'Cloud', 'River', 'Mountain', 'Ocean', 'Forest', 'Desert', 'Storm',
                'Dusk', 'Arrive', 'Cuba', 'Wrote', 'Length', 'Friday', 'Pattern', 'Surprise', 'Shown']

def generate_password():
    # Load words from file
    words = load_wordlist('eff_large_wordlist_002.txt')
    
    # Define separators
    separators = ['!', '@', '$', '%', '^', '&', '*', '-', '_', '+', '=', ':', '|', '~', '?', '/', '.', ';']
    
    # Generate components using secrets
    pair_char = secrets.choice(separators)      # pick one separator char
    start_symbols = pair_char * 2               # repeat it twice for start
    end_symbols = start_symbols                 # use same pair at end
    numbers_start = f"{secrets.randbelow(100):02d}"  # 2 numbers
    numbers_end = f"{secrets.randbelow(100):02d}"    # 2 numbers
    separator = secrets.choice(separators)       # separator symbol
    
    # Select 3 random words using secrets and alternate case
    selected_words = []
    word_list = words.copy()
    # Randomly decide if first word should be upper case
    first_is_upper = bool(secrets.randbelow(2))
    for i in range(3):
        idx = secrets.randbelow(len(word_list))
        word = word_list.pop(idx)
        # Alternate between upper and lower case based on first word
        word = word.upper() if (first_is_upper and i % 2 == 0) or (not first_is_upper and i % 2 == 1) else word.lower()
        selected_words.append(word)
    
    # Construct password
    password = f"{start_symbols}{numbers_start}{separator}{selected_words[0]}{separator}" \
              f"{selected_words[1]}{separator}{selected_words[2]}{separator}{numbers_end}{end_symbols}"
    
    return password

def generate_simple_password():
    # Load words from file
    words = load_wordlist('eff_large_wordlist_002.txt')
    
    # Select 3 random words using secrets and alternate case
    selected_words = []
    word_list = words.copy()
    # Randomly decide if first word should be upper case
    first_is_upper = bool(secrets.randbelow(2))
    for i in range(3):
        idx = secrets.randbelow(len(word_list))
        word = word_list.pop(idx)
        # Alternate between upper and lower case based on first word
        word = word.upper() if (first_is_upper and i % 2 == 0) or (not first_is_upper and i % 2 == 1) else word.lower()
        selected_words.append(word)
    
    # Generate two random numbers
    numbers_mid = f"{secrets.randbelow(100):02d}"
    numbers_end = f"{secrets.randbelow(100):02d}"
    
    # Construct password in the new format: word1+numbers1+word2+numbers2+word3
    password = f"{selected_words[0]}{numbers_mid}{selected_words[1]}{numbers_end}{selected_words[2]}"
    
    return password

def main():
    # Generate and print 3 passwords
    print("\n[*] Generated Passwords:")
    for i in range(3):
        print(f"[*] Password {i+1}: {generate_password()}")
    
    # Generate and print 3 simple passwords
    print("\n[*] Generated Simple Passwords (no special characters):")
    for i in range(3):
        print(f"[*] Simple Password {i+1}: {generate_simple_password()}")
    
if __name__ == "__main__":
    main()

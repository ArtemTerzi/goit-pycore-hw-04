import sys
from pathlib import Path
from show_dir_structure import show_dir_structure
from colorama import Fore

def main():
    file_path = Path(sys.argv[1])
    print(f'{Fore.MAGENTA}{file_path}')
    show_dir_structure(file_path)

if __name__ == '__main__':
    main()
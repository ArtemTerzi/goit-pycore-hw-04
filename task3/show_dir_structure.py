from pathlib import Path
from colorama import Fore, Style

def show_dir_structure(path: Path, indent: str = ""):
    try:
        for el in path.iterdir():
            if el.is_file():
                print(f"{Fore.YELLOW}{indent}  {el.name}{Style.RESET_ALL}")
            elif el.is_dir():
                print(f"{Fore.BLUE}{indent}  {el.name}/{Style.RESET_ALL}")
                show_dir_structure(el, indent + "  ")
    except Exception as e:
        print(f'{Fore.RED}{e}{Style.RESET_ALL}')
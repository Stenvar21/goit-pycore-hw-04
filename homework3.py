import sys
from pathlib import Path
from colorama import Fore
def directory_structure(directory_path):
    path=Path(directory_path)
    if not path.exists() or not path.is_dir():
        print(Fore.RED + f'Шлях {path} не існує, або це не директорія' + Fore.RESET)
        return
    for structure in path.iterdir():
        if structure.is_dir():
            print(Fore.BLUE + {structure.name} + Fore.RESET)
        elif structure.is_file():
            print(      Fore.GREEN + {structure.name} + Fore.RESET)
if len(sys.argv)!=2:
    print(Fore.RED + f"Вкажіть шлях до директорії" + Fore.RESET)
else:
    directory_path=sys.argv(1)
    directory_structure(directory_path)
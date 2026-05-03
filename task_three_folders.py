import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

IGNORE = {".venv", "__pycache__"}

def print_tree(path: Path, prefix: str = "") -> None:
    entries = sorted(
        (e for e in path.iterdir() if e.name not in IGNORE),
        key=lambda e: (e.is_file(), e.name)
    )
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        connector, extension = ("└── ", "    ") if is_last else ("├── ", "│   ")
        name = (
            (Fore.BLUE + Style.BRIGHT + entry.name + "/")
            if entry.is_dir()
            else (Fore.GREEN + entry.name)
        )
        print(Style.DIM + prefix + connector + Style.RESET_ALL + name)
        if entry.is_dir():
            print_tree(entry, prefix + extension)


def main() -> None:
    if len(sys.argv) != 2:
        print(
            "The script was not run correctly - "
            "please specify the file name and provide the path to the directory"
        )
        sys.exit(1)
    path = Path(sys.argv[1])
    if not path.is_dir():
        print(f"Error: '{path}' is not a directory or does not exist.")
        sys.exit(1)
    print(Fore.YELLOW + Style.BRIGHT + path.name + "/")
    print_tree(path)


if __name__ == "__main__":
    main()
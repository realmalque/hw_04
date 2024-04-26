from pathlib import Path

from colorama import Fore
import sys


path = sys.argv[1]
parent_folder_path = Path(path)

def parse_folder(path):
    try:
        for element in path.iterdir():
            if element.is_dir():
                print(Fore.LIGHTBLUE_EX + f"Parse folder: This is folder - {element.name}")
            if element.is_file():
                print(Fore.LIGHTRED_EX + f"Parse folder: This is file - {element.name}")
    except OSError as e:
        print(f"This directory doesn't exist")
parse_folder(parent_folder_path)
# script for MTBL extract pipeline
# by pubins.taylor
# v0.2
# created 02 JUN 2023
# lastUpdate 11 MAY 2024

import concurrent.futures
import subprocess
from tqdm import tqdm


def buildScripts(dirs: list[str]) -> list[tuple]:
    """Builds a list of tuples containing the path to the python executable and the path to the script to run"""
    dirHQ = "/Users/Shared/BaseballHQ/tools"
    scripts: list[tuple] = []
    for _dir in dirs:
        scripts.append((dirHQ + f"/{_dir}/.venv/bin/python", dirHQ + f"/{_dir}/main.py"))
    return scripts


def runScripts(scripts: list[tuple]) -> None:
    """Runs a script using the subprocess module"""
    for _dir, script in tqdm(scripts, total=len(scripts)):
        subprocess.run([_dir, script])


def main():
    # List of scripts to run
    scripts: list[tuple] = buildScripts([
        "Lg_Manager_Getter",
        "Rosters_Getter",
        "Fantasy_Data_Getter",
        "Savant_Data_Getter",
        "Fangraphs_Data_Getter",
    ])

    runScripts(scripts)


if __name__ == '__main__':
    main()

# script for MTBL extract pipeline
# by pubins.taylor
# v0.2
# created 02 JUN 2023
# lastUpdate 11 MAY 2024

import concurrent.futures
import os
import subprocess

import ipdb
from tqdm.asyncio import tqdm


def build_scripts(dirs: list[str]) -> list[tuple]:
    """
    Builds a list of tuples containing the path to the python executable and the path to the
    script to run
    """
    dirHQ = "/Users/Shared/BaseballHQ/tools"
    dirs_cmds_mods: list[tuple] = []
    for _dir in dirs:
        dirs_cmds_mods.append((os.path.join(dirHQ, _dir), ".venv/bin/python", "./app/__main__.py"))

    return dirs_cmds_mods


def run_scripts(scripts: list[tuple]) -> None:
    """
    Runs a script using the subprocess module
    args:
        scripts: list of tuples containing the path to the python executable and the path to the script to run
    """
    for _dir, cmd, mod in tqdm(scripts, total=len(scripts)):
        # activate_venv(_dir)
        # ipdb.set_trace(context=10)
        subprocess.run(
            f"source .venv/bin/activate && PYTHONPATH={_dir} python {mod} && deactivate",
            shell=True, check=True, cwd=_dir)
        # deactivate_venv(_dir)


# def activate_venv(dir: str) -> None:
#     # ipdb.set_trace()
#     activate_script = os.path.join(dir, ".venv", "bin", "activate")
#     subprocess.run(["/bin/bash", f"-c", f"source {activate_script}"])


# def deactivate_venv(dir: str) -> None:
#     # deactivate_script = os.path.join(dir, ".venv", "bin", "deactivate")
#     deactivate_script = "deactivate"
#     subprocess.Popen(['/bin/bash', f'-c', f"{deactivate_script}"], cwd=dir)


def main():
    # List of scripts to run
    scripts: list[tuple] = build_scripts([
        "Lg_Manager_Getter",
        "Rosters_Getter",
        "Fantasy_Data_Getter",
        "Savant_Data_Getter",
        "Fangraphs_Data_Getter",
    ])

    run_scripts(scripts)


if __name__ == '__main__':
    main()

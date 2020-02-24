import subprocess


def get_parsed_os_cmd_output(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True).decode('UTF-8')

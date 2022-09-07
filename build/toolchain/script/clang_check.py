#!/usr/bin/env python3

import os
import sys
import platform
import subprocess


def run_cmd(cmd, **kwargs):
    coding = 'gbk' if platform.system() == "Windows" else 'utf-8'
    res = subprocess.Popen(cmd,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           encoding=coding,
                           **kwargs)
    sout, serr = res.communicate()

    return res.pid, res.returncode, sout, serr


def check_clang_path():
    check_system_cmd = ["clang", "-v"]
    res = run_cmd(check_system_cmd)
    if res[1] == 0 and res[2] != "":
        for installedDir in res[2].split("\n"): # .decode()
            if "InstalledDir" in str(installedDir):
                print(installedDir[14:-4])
    return 0
# 

def check_clang_exists():
    check_system_cmd = ["clang", "-v"]
    res = run_cmd(check_system_cmd)
    if res[1] == 0:
        print(True)
    else:
        print(False)
    return 0


def main():
    if sys.argv[1] == "clang":
        check_clang_path()
    # elif sys.argv[1] == "check":
    #     check_clang_exists()
    else:
        return 0


if __name__ == '__main__':
    sys.exit(main())

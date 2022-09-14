#!/usr/bin/env python3
# coding=utf8
import argparse
import subprocess
import sys
import time


def parse_args():
    """parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--script-file', help='execute script file')
    parser.add_argument('--expect-output', help='expect output')
    parser.add_argument('--timeout-limit', help='timeout limit')
    args = parser.parse_args()
    return args


def print_hi(_args):
    print(f'args is {_args}')
    start_time = time.time()
    cmd = _args.script_file
    if _args.timeout_limit:
        timeout_limit = int(_args.timeout_limit)
    else:
        timeout_limit = 120

    subp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        out, err = subp.communicate(timeout=timeout_limit)
    except subprocess.TimeoutExpired:
        print('Run [', cmd, '] timeout, timeout_limit = ', timeout_limit, 's')
        subp.kill()
        out, err = subp.communicate()

    if _args.expect_output:
        returncode = str(subp.returncode)
        if returncode != _args.expect_output:
            out_str = out.decode('UTF-8')
            err_str = err.decode('UTF-8')
            print(out_str)
            print(err_str)
            print(">>>>> Expect return: [" + _args.expect_output \
                  + "]\n>>>>> But got: [" + returncode + "]")
            raise RuntimeError("Run [" + cmd + "] failed!")
    else:
        raise RuntimeError("Run [" + cmd + "] with no expect !")

    print("Run [" + cmd + "] success!")
    print("used: %.5f seconds" % (time.time() - start_time))


if __name__ == '__main__':
    input_args = parse_args()
    print_hi(input_args)

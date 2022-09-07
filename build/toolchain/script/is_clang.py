#!/usr/bin/env python3
#
# Copyright 2016 Google Inc.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import subprocess

cmd = ["clang", "-v"]
status, result = subprocess.getstatusoutput(" ".join(cmd))
# if ('clang' in str(subprocess.check_output(f'clang --version', shell=False)) and
#     'clang' in str(subprocess.check_output(f'clang++ --version', shell=False))):
if status == 0:
  print('true')
else:
  print('false')

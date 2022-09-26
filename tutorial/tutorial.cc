// Copyright 2020 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include <stdio.h>
#include "exec.h"

int main(int argc, char* argv[]) {
  printf("Hello from the tutorial.\n");
  outprint("uname -a");
  return 0;
}

#!/bin/bash

cd $(dirname $0)
root_path=$(pwd)

while [ $# -gt 0 ];
do
    case $1 in
        -l|--log)
            log="--log"
            shift
            ;;
        -a|--arch)
            shift
            arch="$1"
            shift
            ;;
    esac
done

if [ -n "${arch}" ];then
    build_arch="--args ${arch}"
fi

python3 "${root_path}/build.py" ${log} ${build_arch}

echo -e "\e[32m[RUN INFO]: \c"
echo ""
( out/hello )
echo ""
(file out/hello)
echo -e "\e[0m"

exit 0
gn gen -C out --args="target_cpu=\"arm64\"" && ninja -C out
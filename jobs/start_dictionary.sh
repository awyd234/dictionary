#!/bin/sh
filepath=$(cd "$(dirname "$0")"; pwd)
predir=$(cd "$(dirname "$0")"; cd ..; pwd)
python3 $predir/dictionary/biz/dictionary.py
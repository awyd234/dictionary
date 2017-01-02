#!/bin/sh
predir=$(cd "$(dirname "$0")"; cd ..; pwd)
python3 $predir/dictionary/__main__.py
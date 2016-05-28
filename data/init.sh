#!/bin/bash
#for example
target="localhost"
if [ "$#" -eq 1 ]; then
    target=$1
fi
for f in $(ls *.json); do
    g="/register/${f%.*}"
    echo $g
    http POST http://$target:8000/$g < $f
done

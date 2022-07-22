#!/bin/bash
echo "Found $(find / -type f -name $1 | wc -l) matches"
find / -type f -name $1

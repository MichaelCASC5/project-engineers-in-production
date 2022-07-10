#!/bin/bash
declare -i y=0
while $1; do
	if [[ "$?" -ne 0 ]]
	
	then break

	fi 

	y=$[ y+1 ]
done

echo "It took $y runs to fail"

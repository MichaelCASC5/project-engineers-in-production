#!/bin/bash

count=0

while true; do
	$1 $> tmp
	
	if [[ "$?" - ne 0 ]]
	then
		break
	fi

	count=$[count+1]

done

echo "It took $CNT runs to fail"

cat tmp

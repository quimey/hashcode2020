#!/bin/bash -eux
rm scores.txt || true;
for name in $(ls inputs/); do
	echo $name;
	python3 main.py < inputs/$name > outputs/$name
done
cat scores.txt | paste -sd+ | bc

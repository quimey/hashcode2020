#!/bin/bash -eux
for name in $(ls inputs/); do
	echo $name;
	python3 main.py < inputs/$name > outputs/$name
done

#!/bin/bash -eux
for name in $(ls inputs/); do
	python3 main.py < inputs/$name > outputs/$name
done

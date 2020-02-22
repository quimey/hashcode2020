#!/bin/bash -eux
for name in $(ls inputs/); do
	echo $name;
	./books < inputs/$name > outputs/$name
done

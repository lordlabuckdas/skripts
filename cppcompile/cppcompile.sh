#!/bin/bash
# default code file is code69.cpp
fcode=${1-69}
cp template.cpp code${fcode}.cpp
nvim code${fcode}.cpp
nvim input.txt
g++ code${fcode}.cpp -o code${fcode}.out && ./code${fcode}.out < input.txt

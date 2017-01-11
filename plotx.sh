#!/bin/bash

# this script is used to plot x.dat of all forces in one run, it should be run in the direction the sane as bwd*, fwd* and neut*.

mkdir xfig
for dir in bwd* fwd* neut*
do
    datafile=`find $dir/x_r*`
    echo "
    set term png  size 1280, 720
    set output 'xfig/x$dir.png'
    plot '$datafile'
    " | gnuplot
done
exit 0

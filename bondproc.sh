#!/usr/bin/env bash

# Author: Tee Shern Ren

# usage is "bash bondproc.sh input trajectory.dat bonds.dat > bondtable.dat"

inputfile=$1;
trajfile=$2;
bondfile=$3;

cp oxdna.log oxdna_backup.log

python ../../../UTILS/h_bonds.py $1 $2 \
 | sed -e 's/\s//g' \
 | grep -e '#c' -e '^01' -e '^02' -e '^03' -e '^24' -e '^34' \
 | sed -e 's/^01/b1 /' -e 's/^02/b2 /' -e 's/^03/b3 /' -e 's/^24/m1 /' -e 's/^34/m2 /' > $bondfile;


declare -a list1=($(cat <(grep -nr "#" $bondfile | sed 's/:/ :/' | awk '{print $1}') | tr '\n' ' '));
declare -a list2=($(cat <(grep -nr "#" $bondfile | sed 's/:/ :/' | awk '{print $1}' | sed '1d') <(wc -l <$bondfile)| tr '\n' ' '));

echo "#conf b1 b2 b3 m1 m2"
for ((i=0; i<${#list1[@]}; i++))
do
  for bond in b1 b2 b3 m1 m2
  do
     if grep -q $bond <(sed -n "${list1[$i]},${list2[$i]}p" $bondfile)
     then
        grep $bond <(sed -n "${list1[$i]},${list2[$i]}p" $bondfile) | sed "s/$bond //"
     else
        echo 0
     fi
  done | tr '\n' ' ' | sed "s/^/$(($i+1)) /"; echo " "
done

cp oxdna_backup.log oxdna.log

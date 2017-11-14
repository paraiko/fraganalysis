#!/bin/bash

# skip the first 6 columns (yyyy MM DD HH mm ss)
ctr=7
fname=1
# extract the next 48 columns and write to individual files

while [ $ctr -le 54 ]
do
   name=$(printf "%02d" $fname)
   csvtool col $ctr c1.csv > c1_$name.pir
   ((ctr++))
   ((fname++))
done

echo All done

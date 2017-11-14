#!/bin/bash

# combine all the PIR data files in this directory to one csv file.

# add the first argument as  part of the name

cat *.txt  pir_c$1.csv
# skip the first 6 columns (yyyy MM DD HH mm ss)
ctr=7
fname=1
# extract the next 48 columns and write to individual files

while [ $ctr -le 54 ]
do
   name=$(printf "%02d" $fname)
   csvtool col $ctr pir_c$1.csv > c$1_$name.pir
   ((ctr++))
   ((fname++))
done

echo All done

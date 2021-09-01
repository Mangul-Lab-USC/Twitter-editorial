#!/bin/bash  
  
file='citations.txt'  
  
i=1  
while read line; do  
  
#Reading each line  
echo "Line No. $i : $line"  
/u/home/a/asarkar/.local/bin/icite.py -i citations.txt -H --dir_icite_py /u/scratch/a/asarkarAditya-scratch/twitter/citations -R
rm -rf /u/scratch/a/asarkarAditya-scratch/twitter/citations/*
done < $file
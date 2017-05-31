#!/bin/bash

fqd=/global/projectb/scratch/willsull/Poplar_1000_trees
md=/global/projectb/scratch/willsull/MetaSV_Project/Poplar/Word_Search/fastqs

for file in $(<Poplar_Samples.txt);do
	cd $md
	mkdir $md/$file
	cd $fqd/$file/bwa_dir/fastq_dir
	cp * $md/$file
done

#!/usr/bin/env python

import os

chr18up=False
chr18down=False
chr18del=False
chr1up=False
chr1down=False
chr1del=False
chr5up=False
chr5down=False
chr5del=False

outfile=open("Poplar_Geno_Data.txt","w+")
outfile.write("Sample\tChr18\tChr05\tChr01\n")
files=os.listdir("./alignment_data")
files=sorted(files)

for File in files:
    sample=File[:-15]
    sample_file=open("./alignment_data/%s"% File,"r")
    for lines in sample_file:
        line=lines.strip()
        line=line.split()
        if line[2] == "100M":
            name=line[1].split(":")
            if name[0] == "Chr18":
                if name[2] == "Up_Word":
                    chr18up=True
                elif name[2] == "Down_Word":
                    chr18down=True
                elif name[2] == "Del_Word":
                    chr18del=True
            elif name[0] == "Chr05":
                if name[2] == "Up_Word":
                    chr5up=True
                elif name[2] == "Down_Word":
                    chr5down=True
                elif name[2] == "Del_Word":
                    chr5del=True
            elif name[0] == "Chr01":
                if name[2] == "Up_Word":
                    chr1up=True
                elif name[2] == "Down_Word":
                    chr1down=True
                elif name[2] == "Del_Word":
                    chr1del=True
    sample_file.close()
    if (chr18up or chr18down) and chr18del:
        outfile.write("%s\t0/1\t" % sample)
        chr18up=False
        chr18down=False
        chr18del=False
    elif not chr18del and (chr18up or chr18down):
        outfile.write("%s\t0/0\t" % sample)
        chr18up=False
        chr18down=False
        chr18del=False
    elif chr18del and not (chr18up and chr18down):
        outfile.write("%s\t1/1\t" % sample)
        chr18up=False
        chr18down=False
        chr18del=False
    elif not chr18up and not chr18down and not chr18del:
        outfile.write("%s\tN/A\t" % sample)
    if (chr5up or chr5down) and chr5del:
        outfile.write("0/1\t")
        chr5up=False
        chr5down=False
        chr5del=False
    elif not chr5del and (chr5up or chr5down):
        outfile.write("0/0\t")
        chr5up=False
        chr5down=False
        chr5del=False
    elif chr5del and not (chr5up and chr5down):
        outfile.write("1/1\t")
        chr5up=False
        chr5down=False
        chr5del=False
    elif not chr5up and not chr5down and not chr5del:
        outfile.write("N/A\t")
    if (chr1up or chr1down) and chr1del:
        outfile.write("0/1\n")
        chr1up=False
        chr1down=False
        chr1del=False
    elif not chr1del and (chr1up or chr1down):
        outfile.write("0/0\n")
        chr1up=False
        chr1down=False
        chr1del=False
    elif chr1del and not (chr1up and chr1down):
        outfile.write("1/1\n")
        chr1up=False
        chr1down=False
        chr1del=False
    elif not chr1up and not chr1down and not chr1del:
        outfile.write("N/A\n")
outfile.close()

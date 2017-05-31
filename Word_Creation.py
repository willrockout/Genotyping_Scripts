#!/usr/bin/env python

import argparse
from Bio import SeqIO

def makeArgs():
    parser = argparse.ArgumentParser(
        description="Word Creation for Genotyping")
    parser.add_argument("-SVlist", required=True,
                        help="List of SVs")
    parser.add_argument("-RefFA", required=True,
                        help="Reference Fasta File")
    parser.add_argument("-WordFA", required=True,
                        help="Output fasta name")
    parser.add_argument("-readLength", choices=[75,100],
                        default=100, help="Read length to determine word length [100]")
    return parser
if __name__ == "__main__":
    arguments=makeArgs()
    arguments=arguments.parse_args()
    SVlist=arguments.SVlist
    Ref=arguments.RefFA
    Out=arguments.WordFA
    RL=arguments.readLength

SV_dict={}

SVs=open(SVlist,"r")

for lines in SVs:
    line=lines.strip()
    line=line.split()
    Type=line[0]
    Chrom=line[1]
    SPos=line[2]
    EPos=line[3]
    if Chrom not in SV_dict:
        SV_dict[Chrom]={}
        if Type not in SV_dict[Chrom]:
            SV_dict[Chrom][Type]=[]
            SV_dict[Chrom][Type].append(SPos+":"+EPos)
        else:
            SV_dict[Chrom][Type].append(SPos+":"+EPos)
    else:
        if Type not in SV_dict[Chrom]:
            SV_dict[Chrom][Type]=[]
            SV_dict[Chrom][Type].append(SPos+":"+EPos)
        else:
            SV_dict[Chrom][Type].append(SPos+":"+EPos)
SVs.close()

ref_dict=SeqIO.to_dict(SeqIO.parse(Ref,"fasta"))
    
for chrom in SV_dict:
    for Type in SV_dict[chrom]:
        for coordinates in SV_dict[chrom][Type]:
            positions=coordinates.split(":")
            Spos=positions[0]
            Epos=positions[1]
            if chrom in ref_dict:
                del_word=ref_dict[chrom][(Spos-90):Spos].seq # + ref_dict[chrom][Epos:Epos+90].seq
                print del_word


        

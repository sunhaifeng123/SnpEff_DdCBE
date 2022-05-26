#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input a txt, which contains: T123C",type=str)
parser.add_argument("-r","--ref_name", help="Chromosome Name",type=str)
parser.add_argument("-o","--output", help="Output a vcf file")

args = parser.parse_args()

input_file = args.input
ref_name = args.ref_name
output_file = args.output

output = open(output_file, 'w')


# Read In：

output.write("#CHROM" + '\t' + "POS" + '\t' + "ID" + '\t' + "REF" + '\t' + "ALT" + '\t' + "QUAL" + '\t' + "FILTER" + '\t' + "INFO" + '\n')

with open(input_file, 'r') as input:

    for line in input:

        line = line.strip('\n')

        base1 = line[:1]
        base2 = line[len(line)-1:]
        base_num = line[1:len(line)-1]

        output.write(ref_name + '\t' + base_num + '\t' + '.' + '\t' + base1 + '\t' + base2 + '\t' + '.' + '\t' + '.' + '\t' + '.' + '\n')

print ("Finished!")

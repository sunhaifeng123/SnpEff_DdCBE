# SnpEff_DdCBE
SnpEff_DdCBE

# Step1
python3 Edit_to_Vcf.py -i test.in.txt -r NC_000932.1 -o test.out.vcf

head test.in.txt -n2
T386A
A389T

head test.out.vcf
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO
NC_000932.1     386     .       T       A       .       .       .
NC_000932.1     389     .       A       T       .       .       .


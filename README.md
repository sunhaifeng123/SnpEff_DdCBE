# SnpEff_DdCBE
SnpEff_DdCBE

# Step1
__python3 Edit_to_Vcf.py -i test.in.txt -r NC_000932.1 -o test.out.vcf__

<br/>

```
python3 Edit_to_Vcf.py -h
usage: Edit_to_Vcf.py [-h] [-i INPUT] [-r REF_NAME] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input a txt, which contains: T123C
  -r REF_NAME, --ref_name REF_NAME
                        Chromosome Name
  -o OUTPUT, --output OUTPUT
                        Output a vcf file
```

Input file:
```
head test.in.txt -n2
T386A
A389T
```

Onput file:
```
head test.out.vcf
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO
NC_000932.1     386     .       T       A       .       .       .
NC_000932.1     389     .       A       T       .       .       .
```

# Step2:


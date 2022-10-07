# this code extract amino acid and PLDDT from the pdb file and secondary structure from the data file

import sys
import numpy 

name=sys.argv[1]

pdb_name=name+".pdb"
out_name=name+".out"

file_out=open(out_name,"w+")

with open(pdb_name) as file_pdb:
  for line in file_pdb:
    if line.split()[0]=='ATOM':
      if (line.split()[2]=='CA'):
        print(line.split()[3],line.split()[10])

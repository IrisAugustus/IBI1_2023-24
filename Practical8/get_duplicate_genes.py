'''import re
genes = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
genelist= genes.read()
findup= re.findall(r'.+duplication.+/n',genelist)
print(findup)
dup=str(findup)
find_name=re.findall(r'>.+?_mRNA',dup)
#find_seq=re.findall(r'.+]\n([ATGC]+)\n>.+',genelist)
i=0
for lines in genelist:
    if lines=
content=''
#for i in range(0,len(find_name)+1):
content+=find_name[0]
content+='\n'
content+=find_seq[1]
content+='\n'
i+=1
print(content)

output= open('duplicate_genes.fa', 'w')
output.write(str(findup))
output.close()'''

word ='duplication'
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as input_file, open("duplicate genes.fa", "w") as output_file:
    has_duplication = False
    gene_description =''
    gene_sequence = ''

    for line in input_file:
        if line.startswith('>'):
            if word in line:
                has_duplication = True
                gene_description = line.strip()
                gene_name = gene_description.split()[0][1:]
                output_file.write(f">{gene_name}\n")
            else:
                has_duplication = False
                gene_description =''
                gene_sequence = ''
        elif has_duplication:
            gene_sequence += line.strip()
            output_file.write(line)
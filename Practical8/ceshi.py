import re
genes = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
genelist= genes.read()
genestr=str(genelist)
splited=re.split('>',genestr)
finddup= re.findall(r'.+duplication.+\n',genelist)
dup=str(finddup)
find_name=re.findall(r'>.+?_mRNA',dup)
seqlist=[]
m=0
for i in splited:
    if str(list[0]) in i:
        seq=re.findall(r'^\n[ATGC]+?\n',i)
        print(seq)
        

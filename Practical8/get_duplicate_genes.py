#imput the word to be checked
word ='duplication'
#open the file
with open(r"E:\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as input_file, open(r"E:\IBI1_2023-24\Practical8\duplicate genes.fa", "w") as output_file:
    check_duplication = False
    gene_description =''
    gene_sequence = ''

    for line in input_file:
        if line.startswith('>'):
            #checked if the gene sequence is duplicated, if yes, write its information into the output file
            if word in line:
                check_duplication = True
                gene_description = line.strip()
                gene_name = gene_description.split()[0][1:]
                output_file.write(f">{gene_name}\n")
            #if not duplicated, reset the gene description and sequence
            else:
                check_duplication= False
                gene_description =''
                gene_sequence = ''
        #if it is the sequence line, and has duplication, write into the output file
        elif check_duplication:
            gene_sequence += line.strip()
            output_file.write(line)
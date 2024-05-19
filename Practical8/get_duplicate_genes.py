#The first way to do this.
#set the input file path and the output file path
input_file_path = r"E:/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file_path = r"E:/IBI1_2023-24/Practical8/duplicate_genes.fa"

with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    #set the initial values
    write_mode = False
    current_gene_name = ""
    current_gene_sequence = ""
    #read every line in the input file
    for line in input_file:
        #remove the \n at the end of every line
        line = line.strip() 
        if line.startswith(">"): 
            if write_mode:  
                output_file.write(">" + current_gene_name + "\n")
                output_file.write(current_gene_sequence + "\n")
            write_mode = False  
            #check if there is 'duplication' in the description
            if "duplication" in line:  
                write_mode = True
                #extract the names of the genes
                current_gene_name = line.split()[0][1:]  
                current_gene_sequence = ""  
        elif write_mode:  
            current_gene_sequence += line + "\n" 

    if write_mode:
        output_file.write(">" + current_gene_name + "\n")
        output_file.write(current_gene_sequence)

print("task completed")

'''
#the second way to do this
#input the word to be checked
word ='duplication'
#open the file
with open(r"E:/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as input_file, open(r"E:/IBI1_2023-24/Practical8/duplicate_genes.fa", "w") as output_file:
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
'''

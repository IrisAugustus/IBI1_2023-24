import re
#imput the repetitive sequences to be counted
tips='Please input one of the two repetitive sequences GTGTGT or GTCTGT: '
repeat_patterns = str(input(tips))
#creat a function to count the repetitive sequence, and return the duplicated number
def count_repeats(sequence, patterns):
    total_count = 0
    for pattern in patterns:
        matches = re.finditer(pattern, sequence)
        for match in matches:
            total_count += 1
    return total_count

#import the file path of the file to be used
input_file_path = r'E:\IBI1_2023-24\Practical8\duplicate_genes.fa'
output_file_path = f'E:\IBI1_2023-24\Practical8\{repeat_patterns}_duplicate_genes.fa'

#Open the files
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    gene_name = ''
    sequence = ''
    for line in input_file:
        if line.startswith('>'):
            # get information for the former gene
            if gene_name != '':
                output_file.write(gene_name + ' ' + str(count_repeats(sequence,repeat_patterns)) + '\n' + sequence + '\n\n')
            # get the information of the new gene
            gene_name = line.strip()
            # reset the sequence
            sequence = ''
        else:
            # remove the \n at the end of a line of sequence
            sequence += line.strip()
    # processing the information for the last gene
    if gene_name != '':
        output_file.write(gene_name + ' ' + str(count_repeats(sequence, repeat_patterns)) + '\n' + sequence + '\n')
            
    


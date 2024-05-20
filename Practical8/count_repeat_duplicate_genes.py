import re

# Input the repetitive sequence
tips = 'Please input one of the two repetitive sequences GTGTGT or GTCTGT: '
repeat_pattern = input(tips)

# Validate the input pattern
if repeat_pattern not in ['GTGTGT', 'GTCTGT']:
    print("Invalid input. Please run the script again and input a valid sequence.")
    exit(1)

# Define a function to count the repetitive sequences
def count_repeats(sequence, pattern):
    return len(re.findall(f'(?={pattern})', sequence))

# Set the pathways of the input and output files
input_file_path = r'E:/IBI1_2023-24/Practical8/duplicate_genes.fa'
output_file_path = f'E:/IBI1_2023-24/Practical8/{repeat_pattern}_duplicate_genes.fa'

# Open the files
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    gene_name = ''
    sequence = ''
    for line in input_file:
        if line.startswith('>'):
            if gene_name:
                # Count repeats and write the previous gene sequence to the output file
                count = count_repeats(sequence, repeat_pattern)
                if count!=0:
                    output_file.write(f"{gene_name} {count}\n{sequence}\n\n")
            gene_name = line.strip()
            sequence = ''
        else:
            sequence += line.strip()
    
    # Handle the last gene sequence in the file
    if gene_name:
        count = count_repeats(sequence, repeat_pattern)
        if count!=0:
            output_file.write(f"{gene_name} {count}\n{sequence}\n\n")

print("Task completed")


import re
tips='Please input one of the two repetitive sequences GTGTGT or GTCTGT: '
repeat_patterns = str(input(tips))
def count_repeats(sequence, patterns):
    total_count = 0
    for pattern in patterns:
        matches = re.finditer(pattern, sequence)
        for match in matches:
            total_count += 1
    return total_count


with open('duplicate genes.fa','r') as input_file, open(f'{repeat_patterns}_duplicate_genes.fa','w') as output_file:
    for line in input_file:
        if line.startswith('>'):
            new_line=''
            new_line=line
            output_file.write('\n' + new_line)
        if not line.startswith('>'):
            new_line=''
            new_line+=line.rstrip()
            output_file.write(new_line)
            
            
    

#duplicate_number=count_repeats(line,repeat_patterns)
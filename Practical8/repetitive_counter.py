import re
#input the sequence
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
#input the repetitive pattern
repeat_patterns = ['GTGTGT', 'GTCTGT']
#create a function for counting repetitive numbers
def count_repeats(sequence, patterns):
    total_count = 0
    for pattern in patterns:
        # use lookahead assertions to count overlapping occurrences of specified patterns in a sequence, ways learnt from the Internet
        matches = re.finditer(f'(?={pattern})', sequence)
        for match in matches:
            total_count += 1
    return total_count


total_repeats = count_repeats(seq, repeat_patterns)
print("Total number of repeat elements:", total_repeats)

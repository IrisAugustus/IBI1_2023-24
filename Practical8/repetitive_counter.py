import re
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAAGTGTGTGT'
repeat_patterns = ['GTGTGT', 'GTCTGT']
def count_repeats(sequence, patterns):
    total_count = 0
    for pattern in patterns:
        matches = re.finditer(pattern, sequence)
        for match in matches:
            total_count += 1
    return total_count


total_repeats = count_repeats(seq, repeat_patterns)
print("Total number of repeat elements:", total_repeats)

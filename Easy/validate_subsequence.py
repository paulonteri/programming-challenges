def isValidSubsequence(array, sequence):
    seq_pos = 0
    seq_len = len(sequence)

    # Basic validation of the sequence
    if seq_len == 0 or seq_len > len(array):
        return False

    # Main check
    for i in array:
        if i == sequence[seq_pos]:
            if seq_pos == seq_len - 1:
                return True
            seq_pos += 1
    return False

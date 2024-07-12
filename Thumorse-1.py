def inverse(s):
    return s.translate(str.maketrans('01', '10'))

def thue_morse(n):
    if n == 0:
        return '0'
    else:
        prev_seq = thue_morse(n-1)
        return prev_seq + inverse(prev_seq)
print(thue_morse(2))  
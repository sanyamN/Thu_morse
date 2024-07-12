def replace_symbol(s, symbol, position):
    if symbol == '1':
        if position % 2 == 0:  # even position
            return '321'
        else:  # odd position
            return '123'
    elif symbol == '2':
        if position % 2 == 0:  # even position
            return '132'
        else:  # odd position
            return '231'
    elif symbol == '3':
        if position % 2 == 0:  # even position
            return '213'
        else:  # odd position
            return '312'

def square_free(n):
    if n == 0:
        return '1'
    else:
        prev_seq = square_free(n-1)
        new_seq = ''
        for i, symbol in enumerate(prev_seq):
            new_seq += replace_symbol(prev_seq, symbol, i+1) 
        return new_seq

print(square_free(3))  
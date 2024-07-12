def count_squares(s):
    n = len(s)
    count = 0
    for length in range(1, n // 2 + 1): 
        for i in range(n - 2 * length + 1): 
            if s[i:i+length] == s[i+length:i+2*length]:  
                count += 1

    return count
print(count_squares('1231233'))

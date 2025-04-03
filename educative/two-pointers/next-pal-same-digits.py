def find_next_palindrome(num_str):
    n = len(num_str)
    if n == 1:
        return ""
    half_n = n//2
    if n%2:
        mid = num_str[half_n]
    else:
        mid = ''
    left_half = list(num_str[:half_n])
    
    #two pointer
    i = len(left_half)-2
    while i >= 0 and left_half[i] >= left_half[i+1]:
        i -= 1
    if i == -1:
        return ""
    
    j = len(left_half)-1
    while left_half[j] <= left_half[i]:
        j -= 1
    
    left_half[i], left_half[j] = left_half[j], left_half[i]
    left_half[i + 1:] = reversed(left_half[i + 1:])
    lh_string = ''.join(left_half)
    sol = lh_string
    sol += mid
    sol += lh_string[::-1]
    return sol

num_str = "23143034132"
print(find_next_palindrome(num_str))
     
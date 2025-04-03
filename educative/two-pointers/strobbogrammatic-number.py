# Given a string num representing an integer, determine whether it is a strobogrammatic number. Return TRUE if the number is strobogrammatic or FALSE if it is not.

# Note: A strobogrammatic number appears the same when rotated 
# 180 degrees (viewed upside down). For example, “69” is strobogrammatic because it looks the same when flipped upside down, while “962” is not.

def is_strobogrammatic(num):
    l, r = 0, len(num)-1
    
    while l <= r:
        if isNotStrob(num[l], num[r]):
            return False
        l += 1; r -= 1
        
    return True
        

def isNotStrob(n1, n2):
    if (n1 == '1' and n2 == '1') or (n1 == '6' and n2 == '9') or (n2 == '6' and n1 == '9') or (n1 == '0' and n2 == '0') or (n1 == '8' and n2 == '8'):
        return False
    return True

num = "123"
print(is_strobogrammatic(num))
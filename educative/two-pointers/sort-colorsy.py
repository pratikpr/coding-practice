# Given an array, colors, which contains a combination of the following three elements:
# 0 (representing red)
# 1 (representing white)
# 2 (representing blue)

# Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue. To improve your problem-solving skills, do not utilize the built-in sort function.

def sort_colors(colors):
    arr = colors
    l,r,i = 0, len(colors)-1, 0
    
    while i <= r:
        # print(arr[i],arr, i, l, r)
        if colors[i] == 1:
            i += 1
        elif colors[i] == 0:
            colors[l], colors[i] = colors[i], colors[l]
            i += 1
            l += 1
        else:
            colors[r], colors[i] = colors[i], colors[r]
            r -= 1     
    return colors

colors = [0,1,0]
print(sort_colors(colors))

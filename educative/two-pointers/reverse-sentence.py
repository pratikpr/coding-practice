# Given a sentence, reverse the order of its words without affecting the order of letters within the given word.

def reverse_words(sentence):
    sentence = sentence.strip()
    s_arr = sentence.split()
    l, r = 0, len(s_arr)-1

    while l < r:
        s_arr[l], s_arr[r] = s_arr[r], s_arr[l]
        l += 1; r -= 1
    return ' '.join(s_arr)

sentence = "Hello     World"
print(reverse_words(sentence))
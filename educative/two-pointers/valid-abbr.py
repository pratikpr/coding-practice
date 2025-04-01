# Given a string word and an abbreviation abbr, return TRUE if the abbreviation matches the given string. Otherwise, return FALSE.

def valid_word_abbreviation(word, abbr):
    w, a = 0, 0
    
    while a < len(abbr):
        if abbr[a].isalpha():
            if w >= len(word) or word[w] != abbr[a]:
                return False
            w += 1; a += 1
        elif abbr[a].isdigit():
            if abbr[a] == '0':
                return False
            start = a
            while a < len(abbr) and abbr[a].isdigit():
                a += 1
            n = int(abbr[start:a]) 
            w += n
            
    return w == len(word) and a == len(abbr)

word = "computation"
abbr = "compu03on"
print(valid_word_abbreviation(word, abbr))

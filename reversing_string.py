def reverse_string(s):
    string=""
    for i in range(len(s)-1,-1, -1):
        string=f"{string}{s[i]}"
    return string
print(reverse_string("The quick brown fox jumped over the lazy dog."))
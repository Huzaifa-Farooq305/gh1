from spliting_string import split_string
def longest_even_word(s):
    split=split_string(s)
    max=""
    for item in split:
        if len(item)>len(max) and len(item)%2==0:
            max=item
    return max
print(longest_even_word("I saw a dog that was hungry and thirsty"))
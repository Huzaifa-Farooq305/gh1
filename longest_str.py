from spliting_string import split_string
def longest_string(s):
    spli=split_string(s)
    max=""
    for item in spli:
        if len(item)>len(max):
            max=item
    return max
print(longest_string("I saw a dog that was hungry and and thirsty"))
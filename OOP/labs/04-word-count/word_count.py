


word_count = 0
space_count = 0
with open('example.txt', 'r') as f:
    word_len = 0
    for line in f:
        for c in line:
            if c == ' ':
                space_count += 1
            # use space and line break as end of the word
            if c != ' ' and c != '\n':
                word_len += 1
            else:
                # when we encounter space or line break it means that
                # this is the end of the current word
                # we also consider case of consecutive spaces
                # and take only non empty words
                if word_len > 0:
                    word_count += 1
                word_len = 0
if word_len > 0:
    word_count += 1

print("Word count is:", word_count)
print("Space count is:", space_count)
        

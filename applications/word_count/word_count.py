import re

def word_count(s):
    # Your code here

    # Case should be ignored. Output keys must be lowercase.
    # key order in dict doesn't matter
    # split the string into words on any whitespace
    # ignore each of the following chars:
    # " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    # if input contains only ignored chars, return empty dict

    word_dict = {}

    # loop through string and split()
    for word in s.split():
        # lowercase each word
        lowercase_word = word.lower()
        new_word = re.sub('[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}(\)\*\^\&]', '', lowercase_word)
        # print(reject)

        if len(new_word ) > 0:
            if new_word  not in word_dict:
                word_dict[new_word ] = 1
            else:
                word_dict[new_word ] +=1

    return word_dict

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
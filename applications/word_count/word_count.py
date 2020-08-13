def word_count(s):
    # Your code here

    # Case should be ignored. Output keys must be lowercase.
    # key order in dict doesn't matter
    # split the string into words on any whitespace
    # ignore each of the following chars:
    # " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    # if input contains no ignored chars, return empty dict

    word_dict = {}

    # if input contains no ignored chars
    #     return empty dict
    #


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
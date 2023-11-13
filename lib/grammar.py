def grammar(string):
    punctuation=['!','.','?']
    if string[0].isupper() and string[-1] in punctuation:
        return True
    else:
        return False


# string='hello world'
# print(string[0])
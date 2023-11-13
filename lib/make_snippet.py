def make_snippet(string):
    string_length = len(string.split(' '))
    result=''
    if string_length <=5:
        return string
    else:
        for i in range(0,5):
            result+=string.split(' ')[i]+' '
    return result + '...'

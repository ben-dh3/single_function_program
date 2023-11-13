def check_todo(string):
    for word in string.split(' '):
        if word == '#TODO':
            return True
    return False
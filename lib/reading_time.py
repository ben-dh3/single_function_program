# Function signiture
# 200 words = 1 minute
# 3.33 words per second

def reading_time(string):
    # counts words in a string
    string_length = len(string.split(' '))
    time_count = string_length/200
    time_seconds = time_count*60
    # // divides and rounds up
    time_hours= time_seconds // 3600
    time_minutes = time_seconds // 60
    formatted_time = ("%d:%02d:%02d" % (time_hours, time_minutes, time_seconds))
    return formatted_time
#     # divide length of string by 200
#     # convert into minutes and seconds
#     # return 

# string = 'this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for this is a long string and is the test for'
# print(len(string.split(' ')))



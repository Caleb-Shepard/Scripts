import sys

# memory is free so do the same thign twice amirite
message = ""
for arg in sys.argv[1:]:
    message += str(arg) + " "

# hehehehehehhh B) 
for char in message:
    if char.lower() is 'b':
        print(":b:", end=' ')
    elif char.isalpha():
        print(":regional_indicator_" + char.lower() + ":", end=' ')
    elif char is ' ':
        print("   ", end='')
    elif char is '!':
        print(":exclamation:", end=' ')
    else:
        print(char, end='')

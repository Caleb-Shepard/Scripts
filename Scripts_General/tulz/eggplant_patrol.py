import sys

# memory is free so do the same thign twice amirite
message = ""
for arg in sys.argv[1:]:
    message += str(arg) + " "


# hehehehehehhh B) 
for char in message:
    if char.isalpha():
        # gift me squars NIX
        if char.lower() == 'b':
            print(":b:", end = ' ')
        else:
            print(":regional_indicator_" + char.lower() + ":", end=' ')
    elif char.isnumeric():
        if char is '1':
            print(":one:", end=' ')
        elif char is '2':
            print(":two:", end=' ')
        elif char is '3':
            print(":three:", end=' ')
        elif char is '4':
            print(":four:", end=' ')
        elif char is '5':
            print(":five:", end=' ')
        elif char is '6':
            print(":six:", end=' ')
        elif char is '7':
            print(":seven:", end=' ')
        elif char is '8':
            print(":eight:", end=' ')
        elif char is '9':
            print(":nine:", end=' ')
        elif char is '0':
            print(":zero:", end=' ')
        else: # <should be> unneccessary case
            print(char, end='')
    elif char is ' ':
        print("   ", end='')
    elif char is '!':
        print(":exclamation:", end=' ')
    else:
        print(char, end='')

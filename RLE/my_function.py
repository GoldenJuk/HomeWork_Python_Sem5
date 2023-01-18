def coding(my_string):
    coding = ""
    i = 0
    while i < len(my_string):
        count = 1
        while i + 1 < len(my_string) and my_string[i] == my_string[i + 1]:
            count = count + 1
            i = i + 1
        coding += str(count) + my_string[i]
        i = i + 1
    return coding

def decoding(my_string):
    count = ''
    decoding = ''
    for char in my_string:
        if char.isdigit():
            count += char 
        else:
            decoding += char * int(count)
            count = ''
    return decoding